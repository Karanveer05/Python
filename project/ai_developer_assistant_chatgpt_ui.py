
import json
import os
import time
import uuid
import html
import logging
from datetime import datetime
import ollama
import streamlit as st
import streamlit.components.v1 as components

History_File="history.jsonl"
Default_Model_Name="llama3.2:3b"
count=1

logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

st.set_page_config(
    page_title="AI Developer Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

if "Model_Name" not in st.session_state:
    st.session_state.Model_Name=Default_Model_Name
if "Current_Chat_Id" not in st.session_state:
    st.session_state.Current_Chat_Id=str(uuid.uuid4())
if "Current_Mode" not in st.session_state:
    st.session_state.Current_Mode="Answer Questions"
if "History_lines" not in st.session_state:
    st.session_state.History_lines=0
if "Dark_Mode" not in st.session_state:
    st.session_state.Dark_Mode=True
if "Program_Status" not in st.session_state:
    st.session_state.Program_Status=None
if "Generating" not in st.session_state:
    st.session_state.Generating=False
if "Stop_Generation" not in st.session_state:
    st.session_state.Stop_Generation=False
if "Show_History" not in st.session_state:
    st.session_state.Show_History=False

def apply_theme():
    if st.session_state.Dark_Mode:
        background="#212121"
        sidebar="#171717"
        card="#2f2f2f"
        text="#ececec"
        muted="#a6a6a6"
        border="#3f3f3f"
        input_bg="#2f2f2f"
        hover="#383838"
    else:
        background="#ffffff"
        sidebar="#f7f7f8"
        card="#ffffff"
        text="#202123"
        muted="#6b6b6b"
        border="#e5e5e5"
        input_bg="#ffffff"
        hover="#eeeeee"
    st.markdown(f"""
    <style>
    .stApp {{
        background:{background};
        color:{text};
    }}
    [data-testid="stSidebar"] {{
        background:{sidebar};
        border-right:1px solid {border};
    }}
    [data-testid="stSidebar"] * {{
        color:{text};
    }}
    .block-container {{
        max-width:900px;
        padding-top:1.2rem;
        padding-bottom:7rem;
    }}
    h1,h2,h3,p,span,label {{
        color:{text};
    }}
    .app-header {{
        display:flex;
        align-items:center;
        justify-content:space-between;
        gap:1rem;
        margin-bottom:.5rem;
    }}
    .app-title {{
        font-size:1.35rem;
        font-weight:700;
        color:{text};
    }}
    .app-subtitle {{
        color:{muted};
        font-size:.88rem;
        margin-top:.2rem;
    }}
    .welcome-title {{
        text-align:center;
        font-size:2rem;
        font-weight:700;
        margin-top:10vh;
        margin-bottom:.4rem;
        color:{text};
    }}
    .welcome-subtitle {{
        text-align:center;
        color:{muted};
        margin-bottom:1.5rem;
    }}
    .mode-card {{
        min-height:108px;
        padding:16px;
        border:1px solid {border};
        border-radius:16px;
        background:{card};
        color:{text};
    }}
    .mode-card:hover {{
        background:{hover};
    }}
    .chat-meta {{
        color:{muted};
        font-size:.8rem;
        margin-bottom:.8rem;
    }}
    [data-testid="stChatInput"] {{
        background:{input_bg};
        border:1px solid {border};
        border-radius:18px;
    }}
    [data-testid="stChatMessage"] {{
        background:transparent;
    }}
    div[data-testid="stButton"] > button {{
        border-radius:10px;
    }}
    .sidebar-section {{
        color:{muted};
        font-size:.75rem;
        text-transform:uppercase;
        letter-spacing:.06em;
        margin:.7rem 0 .35rem 0;
    }}
    </style>
    """, unsafe_allow_html=True)

def ensure_history_file():
    if not os.path.exists(History_File):
        with open(History_File,"w",encoding="utf-8") as file:
            pass

def load_history_records():
    ensure_history_file()
    records=[]
    try:
        with open(History_File,"r",encoding="utf-8") as file:
            for line in file:
                line=line.strip()
                if line=="":
                    continue
                message=json.loads(line)
                if "chat_id" not in message:
                    message["chat_id"]="legacy-chat"
                if "mode" not in message:
                    message["mode"]="Answer Questions"
                if "created_at" not in message:
                    message["created_at"]=""
                records.append(message)
        return records
    except Exception as Error:
        logging.error(f"History loading failed: {Error}")
        return []

def save_all_history_records(records):
    with open(History_File,"w",encoding="utf-8") as file:
        for record in records:
            json.dump(record,file,ensure_ascii=False)
            file.write("\n")

def previous_content(chat_id=None,exclude_last_exchange=False):
    try:
        if chat_id is None:
            chat_id=st.session_state.Current_Chat_Id
        records=[record for record in load_history_records() if record.get("chat_id") == chat_id]
        if exclude_last_exchange and len(records)>=2:
            records=records[:-2]
        content=""
        for message in records:
            content+=f"{message['role']} : {message['content']} \n"
            if message["role"]=="Assistant":
                content+="\n"
        return content
    except Exception as Error:
        logging.error(f"Previous content loading failed: {Error}")
        return ""

def get_installed_models():
    try:
        response=ollama.list()
        model_items=getattr(response,"models",None)
        if model_items is None and isinstance(response,dict):
            model_items=response.get("models",[])
        model_names=[]
        for item in model_items or []:
            model_name=getattr(item,"model",None) or getattr(item,"name",None)
            if model_name is None and isinstance(item,dict):
                model_name=item.get("model") or item.get("name")
            if model_name:
                model_names.append(model_name)
        if st.session_state.Model_Name not in model_names:
            model_names.insert(0,st.session_state.Model_Name)
        return list(dict.fromkeys(model_names))
    except Exception as error:
        logging.error(f"Unable to list Ollama models: {error}")
        return [st.session_state.Model_Name]

def Ollama_model_stream(input_data,System_instructions,history_override=None):
    global count
    history=previous_content() if history_override is None else history_override
    try:
        data=history+"\n\n"+input_data
        stream=ollama.chat(
            model=st.session_state.Model_Name,
            messages=[
                {"role":"system","content":System_instructions},
                {"role":"user","content":data}
            ],
            stream=True
        )
        count=1
        for chunk in stream:
            if st.session_state.Stop_Generation:
                break
            content=getattr(getattr(chunk,"message",None),"content",None)
            if content is None and isinstance(chunk,dict):
                content=chunk.get("message",{}).get("content","")
            if content:
                yield content
    except Exception as error:
        if count<4:
            logging.error(f"Error :Ollama Request failed Attempt {count} : {error}")
            count+=1
            time.sleep(2)
            yield from Ollama_model_stream(input_data,System_instructions,history_override)
        else:
            logging.error(f"Ollama Request failed after maximum attempts: {error}")
            count=1
            raise error

def Program_check_function():
    try:
        response=ollama.chat(
            model=st.session_state.Model_Name,
            messages=[{"role":"user","content":"Reply only with OK"}]
        )
        content=getattr(getattr(response,"message",None),"content",None)
        if content is None and isinstance(response,dict):
            content=response.get("message",{}).get("content","")
        if content:
            logging.info("Ollama model Connection Build Successfully")
            return True
        return False
    except Exception as error:
        logging.error(f"Ollama model connection failed: {error}")
        return False

def get_current_chat_records():
    return [
        record for record in load_history_records()
        if record.get("chat_id")==st.session_state.Current_Chat_Id
    ]

def get_chat_title(records):
    for record in records:
        if record.get("role")=="user" and record.get("content","").strip():
            title=record["content"].replace("\n"," ").strip()
            return title[:34]+("..." if len(title)>34 else "")
    return "New chat"

def get_all_chats():
    chats={}
    for record in load_history_records():
        chat_id=record.get("chat_id","legacy-chat")
        chats.setdefault(chat_id,[]).append(record)
    items=[]
    for chat_id,records in chats.items():
        if not records:
            continue
        created=records[-1].get("created_at","")
        items.append((chat_id,get_chat_title(records),created))
    items.sort(key=lambda item:item[2],reverse=True)
    return items

def conversation_save_function(result,data,mode=None):
    if result is None or result is False:
        return
    if mode is None:
        mode=st.session_state.Current_Mode
    created_at=datetime.now().isoformat(timespec="seconds")
    with open(History_File,"a",encoding="utf-8") as file:
        json.dump({
            "chat_id":st.session_state.Current_Chat_Id,
            "role":"user",
            "content":data,
            "mode":mode,
            "created_at":created_at
        },file,ensure_ascii=False)
        file.write("\n")
        json.dump({
            "chat_id":st.session_state.Current_Chat_Id,
            "role":"Assistant",
            "content":result,
            "mode":mode,
            "created_at":created_at
        },file,ensure_ascii=False)
        file.write("\n")
    st.session_state.History_lines+=2
    logging.info("Conversation saved successfully")

def update_last_assistant_response(new_result):
    records=load_history_records()
    for index in range(len(records)-1,-1,-1):
        if records[index].get("chat_id")==st.session_state.Current_Chat_Id and records[index].get("role")=="Assistant":
            records[index]["content"]=new_result
            records[index]["created_at"]=datetime.now().isoformat(timespec="seconds")
            save_all_history_records(records)
            return True
    return False

def Clear_Current_history():
    records=load_history_records()
    filtered=[
        record for record in records
        if record.get("chat_id")!=st.session_state.Current_Chat_Id
    ]
    if len(filtered)==len(records):
        return False
    save_all_history_records(filtered)
    st.session_state.History_lines=0
    st.session_state.Current_Chat_Id=str(uuid.uuid4())
    logging.info("Current chat history deleted successfully")
    return True

def new_chat_function():
    st.session_state.Current_Chat_Id=str(uuid.uuid4())
    st.session_state.Current_Mode="Answer Questions"
    st.session_state.History_lines=0
    st.session_state.Show_History=False
    st.session_state.Stop_Generation=False

def select_chat_function(chat_id):
    st.session_state.Current_Chat_Id=chat_id
    records=[
        record for record in load_history_records()
        if record.get("chat_id")==chat_id
    ]
    if records:
        st.session_state.Current_Mode=records[-1].get("mode","Answer Questions")
    st.session_state.Show_History=False

def system_instruction_for_mode(mode):
    if mode=="Answer Questions":
        return "Answer the user's question clearly and accurately. Keep the explanation beginner-friendly, useful and focused."
    if mode=="Explain Code":
        return "You are a programming tutor. Explain the provided code in beginner-friendly language. Explain its purpose, important concepts, flow and possible issues. Do not over-explain."
    if mode=="Generate Code":
        return "Generate clean and working code based on the user's request. Make the code easy to copy. Keep unnecessary explanation short and place code in proper Markdown code blocks."
    if mode=="Summarize Text":
        return "Summarize the provided text clearly in 4-5 concise lines unless the user asks for another format. Preserve the important meaning and key points."
    return "Answer clearly and helpfully."

def placeholder_for_mode(mode):
    if mode=="Answer Questions":
        return "Message AI Developer Assistant..."
    if mode=="Explain Code":
        return "Paste code here and ask me to explain it..."
    if mode=="Generate Code":
        return "Describe the code you want to generate..."
    if mode=="Summarize Text":
        return "Paste text here to summarize..."
    return "Message AI Developer Assistant..."

def display_current_chat():
    records=get_current_chat_records()
    for record in records:
        role="assistant" if record.get("role")=="Assistant" else "user"
        with st.chat_message(role):
            st.markdown(record.get("content",""))

def chat_download_text():
    records=get_current_chat_records()
    lines=[]
    for record in records:
        lines.append(f"{record.get('role','')}: {record.get('content','')}")
        lines.append("")
    return "\n".join(lines)

def copy_button(text,key_name):
    safe_text=json.dumps(text)
    components.html(
        f"""
        <button id="{key_name}" style="
            border:1px solid #555;
            border-radius:8px;
            padding:6px 10px;
            background:transparent;
            color:inherit;
            cursor:pointer;
            font-size:12px;">
            Copy response
        </button>
        <script>
        const btn=document.getElementById({json.dumps(key_name)});
        btn.onclick=async()=>{{
            await navigator.clipboard.writeText({safe_text});
            btn.innerText='Copied';
            setTimeout(()=>btn.innerText='Copy response',1200);
        }};
        </script>
        """,
        height=40
    )

def generate_response(input_data,mode,history_override=None):
    st.session_state.Stop_Generation=False
    st.session_state.Generating=True
    system_instructions=system_instruction_for_mode(mode)
    response_placeholder=st.empty()
    full_response=""
    try:
        for chunk in Ollama_model_stream(input_data,system_instructions,history_override):
            full_response+=chunk
            response_placeholder.markdown(full_response+"▌")
        response_placeholder.markdown(full_response)
        return full_response
    except Exception as error:
        response_placeholder.error(f"Ollama request failed: {error}")
        return False
    finally:
        st.session_state.Generating=False
        st.session_state.Stop_Generation=False

apply_theme()
ensure_history_file()

with st.sidebar:
    st.markdown("## 🤖 AI Developer Assistant")
    st.caption("Local AI • Ollama")
    if st.button("＋ New chat",use_container_width=True):
        new_chat_function()
        st.rerun()
    st.session_state.Dark_Mode=st.toggle(
        "Dark mode",
        value=st.session_state.Dark_Mode
    )
    st.markdown('<div class="sidebar-section">Previous chats</div>',unsafe_allow_html=True)
    chats=get_all_chats()
    if not chats:
        st.caption("No previous chats yet.")
    for chat_id,title,created in chats[:30]:
        active=chat_id==st.session_state.Current_Chat_Id
        label=("● " if active else "")+title
        if st.button(label,key=f"chat_{chat_id}",use_container_width=True):
            select_chat_function(chat_id)
            st.rerun()
    st.markdown('<div class="sidebar-section">Chat tools</div>',unsafe_allow_html=True)
    if st.button("🗑️ Clear Current History",use_container_width=True):
        if Clear_Current_history():
            st.success("Current chat cleared.")
            st.rerun()
        else:
            st.info("This chat has no saved history.")
    download_text=chat_download_text()
    st.download_button(
        "⬇️ Download chat",
        data=download_text,
        file_name="ai_developer_assistant_chat.txt",
        mime="text/plain",
        use_container_width=True,
        disabled=not bool(download_text.strip())
    )
    if st.button("🔌 Test Ollama",use_container_width=True):
        with st.spinner("Checking Ollama..."):
            st.session_state.Program_Status=Program_check_function()
        if st.session_state.Program_Status:
            st.success("Ollama connected.")
        else:
            st.error("Ollama connection failed.")

installed_models=get_installed_models()
header_left,header_right=st.columns([3,2])
with header_left:
    st.markdown('<div class="app-title">AI Developer Assistant</div>',unsafe_allow_html=True)
    st.markdown('<div class="app-subtitle">Ask, explain, generate and summarize with a local Ollama model.</div>',unsafe_allow_html=True)
with header_right:
    selected_model=st.selectbox(
        "Model",
        installed_models,
        index=installed_models.index(st.session_state.Model_Name) if st.session_state.Model_Name in installed_models else 0,
        label_visibility="collapsed"
    )
    if selected_model!=st.session_state.Model_Name:
        st.session_state.Model_Name=selected_model
        st.session_state.Program_Status=None
        st.rerun()

mode_options=[
    "Answer Questions",
    "Explain Code",
    "Generate Code",
    "Summarize Text"
]
st.session_state.Current_Mode=st.segmented_control(
    "Mode",
    options=mode_options,
    default=st.session_state.Current_Mode if st.session_state.Current_Mode in mode_options else "Answer Questions",
    label_visibility="collapsed"
) or "Answer Questions"

current_records=get_current_chat_records()

if not current_records:
    st.markdown('<div class="welcome-title">How can I help you today?</div>',unsafe_allow_html=True)
    st.markdown('<div class="welcome-subtitle">Choose a mode or start typing below.</div>',unsafe_allow_html=True)
    card1,card2=st.columns(2)
    with card1:
        st.markdown('<div class="mode-card"><b>💬 Ask a question</b><br><br>Learn concepts, solve problems, or get clear explanations.</div>',unsafe_allow_html=True)
        if st.button("Use Answer Questions",use_container_width=True):
            st.session_state.Current_Mode="Answer Questions"
            st.rerun()
    with card2:
        st.markdown('<div class="mode-card"><b>💻 Explain code</b><br><br>Paste code directly into the chat box and understand how it works.</div>',unsafe_allow_html=True)
        if st.button("Use Explain Code",use_container_width=True):
            st.session_state.Current_Mode="Explain Code"
            st.rerun()
    card3,card4=st.columns(2)
    with card3:
        st.markdown('<div class="mode-card"><b>⚙️ Generate code</b><br><br>Describe what you want to build and generate a starting solution.</div>',unsafe_allow_html=True)
        if st.button("Use Generate Code",use_container_width=True):
            st.session_state.Current_Mode="Generate Code"
            st.rerun()
    with card4:
        st.markdown('<div class="mode-card"><b>📝 Summarize text</b><br><br>Paste long text and receive a concise summary.</div>',unsafe_allow_html=True)
        if st.button("Use Summarize Text",use_container_width=True):
            st.session_state.Current_Mode="Summarize Text"
            st.rerun()
else:
    display_current_chat()

if st.session_state.Program_Status is False:
    st.error("Ollama is not connected. Open Ollama and confirm the selected model is installed.")
    st.code("ollama list",language="powershell")

current_records=get_current_chat_records()
last_user=None
last_assistant=None
if current_records:
    for record in reversed(current_records):
        if last_assistant is None and record.get("role")=="Assistant":
            last_assistant=record
        if record.get("role")=="user":
            last_user=record
            break

if last_assistant:
    action1,action2,action3=st.columns([1,1,4])
    with action1:
        copy_button(last_assistant.get("content",""),"copy_last_response")
    with action2:
        if st.button("↻ Regenerate"):
            history_override=previous_content(st.session_state.Current_Chat_Id,exclude_last_exchange=True)
            with st.chat_message("assistant"):
                new_result=generate_response(
                    last_user.get("content",""),
                    last_user.get("mode",st.session_state.Current_Mode),
                    history_override
                )
            if new_result:
                update_last_assistant_response(new_result)
                st.rerun()
    with action3:
        if st.session_state.Generating:
            if st.button("⏹ Stop generation"):
                st.session_state.Stop_Generation=True
                st.rerun()

user_input=st.chat_input(
    placeholder_for_mode(st.session_state.Current_Mode),
    disabled=st.session_state.Generating
)

if user_input:
    with st.chat_message("user"):
        st.markdown(user_input)
    with st.chat_message("assistant"):
        result=generate_response(
            user_input,
            st.session_state.Current_Mode
        )
    if result:
        conversation_save_function(
            result,
            user_input,
            st.session_state.Current_Mode
        )
        st.rerun()
