from jobs_data import jobs

print("=" * 70)
print(" AI TECH STACK RECOMMENDER USING RAW SKILLS ")
print("=" * 70)

name = input("Enter Your Name: ")

career_goal = input(
    "Enter Career Goal (AI / Data / Web / DevOps / Security): "
)

skills = input(
    "\nEnter Skills Separated By Commas:\n"
).lower().split(",")

skills = [skill.strip() for skill in skills]

results = []

for job, details in jobs.items():

    required_skills = details["skills"]

    matched = []
    missing = []

    for skill in required_skills:

        if skill in skills:
            matched.append(skill)
        else:
            missing.append(skill)

    score = (
        len(matched) /
        len(required_skills)
    ) * 100

    results.append(
        {
            "job": job,
            "score": score,
            "matched": matched,
            "missing": missing,
            "salary": details["salary"],
            "stack": details["tech_stack"]
        }
    )

results.sort(
    key=lambda x: x["score"],
    reverse=True
)

print("\n")
print("=" * 70)
print(" TOP RECOMMENDATIONS ")
print("=" * 70)

for index, result in enumerate(results[:3], start=1):

    print(f"\nRank #{index}")
    print("-" * 50)

    print(
        f"Job Role : {result['job']}"
    )

    print(
        f"Match Score : {result['score']:.2f}%"
    )

    print(
        f"Expected Salary : {result['salary']}"
    )

    print(
        "\nMatched Skills:"
    )

    if len(result["matched"]) == 0:
        print("None")
    else:
        for skill in result["matched"]:
            print("✓", skill)

    print(
        "\nMissing Skills:"
    )

    if len(result["missing"]) == 0:
        print("None")
    else:
        for skill in result["missing"]:
            print("✗", skill)

    print(
        "\nRecommended Tech Stack:"
    )

    for tech in result["stack"]:
        print("•", tech)

best = results[0]

print("\n")
print("=" * 70)
print(" BEST MATCH ")
print("=" * 70)

print(
    f"Congratulations {name}!"
)

print(
    f"Best Recommended Career: {best['job']}"
)

print(
    f"Match Score: {best['score']:.2f}%"
)

print(
    f"Expected Salary: {best['salary']}"
)

print("\nLearning Roadmap")

for skill in best["missing"]:
    print("Learn ->", skill)

with open(
    "recommendations.txt",
    "w",
    encoding="utf-8"
) as file:

    file.write(
        "TECH STACK RECOMMENDATION REPORT\n"
    )

    file.write(
        "=" * 50 + "\n"
    )

    file.write(
        f"Name : {name}\n"
    )

    file.write(
        f"Best Career : {best['job']}\n"
    )

    file.write(
        f"Match Score : {best['score']:.2f}%\n"
    )

    file.write(
        f"Salary : {best['salary']}\n\n"
    )

    file.write(
        "Missing Skills:\n"
    )

    for skill in best["missing"]:
        file.write(
            "- " + skill + "\n"
        )

print(
    "\nReport Generated Successfully!"
)

print(
    "File Saved As recommendations.txt"
)