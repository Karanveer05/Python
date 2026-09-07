import json
with open("resume_evaluation.jsonl", "r") as file:
        data =[]
        for line in file:
            data.append(json.loads(line))  
        sorted_candidates = sorted(data, key=lambda x: x['skill_match_score'], reverse=True)
        print("\nCandidates sorted by skill match score:")
        for candidate in sorted_candidates:
            print(f"Candidate Name: {candidate['candidate_name']}, Skill Match Score: {candidate['skill_match_score']}")
        top_candidate = sorted_candidates[0]
        print("\nTop Candidate:")
        print(f"Name: {top_candidate['candidate_name']}, Skill Match Score: {top_candidate['skill_match_score']}")