import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import sys
import subprocess


job_levels = {
        "EN": "Entry Level",
        "MI": "Mid Level",
        "SE": "Senior Level",
        "EX": "Executive/Director Level"
    }

#1
def job_level_pie_chart(df, directory):
    '''
    Show pie chart of job categories for your job level of interest.
    Entry level = EN
    Mid level = MI
    Senior level = SE
    Executive/director level = EX
    '''

    print("-------------1-------------")
    print("Display the Job Title Distribution by Category in computer science specified experience levels...")
    print("-------------1-------------")
    time.sleep(2)
    print("\nPlease specify which experience levels you are more interested in:")
    for code, desc in job_levels.items():
        print(f"{desc} = {code}")

    # Ask for multiple selections, comma-separated
    levels_input = input(
        "\nPlease select your job level(s) of interest (comma-separated, e.g., EN,MI,SE). Feel free to choose all of them: "
    ).strip().upper()

    # Split input into list and clean spaces
    selected_levels = [lvl.strip() for lvl in levels_input.split(",") if lvl.strip() in job_levels]

    if not selected_levels:
        print("No valid job levels entered. Exiting Program...")
        sys.exit()

    figures=[]
    for level in selected_levels:
        df_level = df[df["experience_level"] == level]
        # Categorize jobs
        data_jobs = df_level[df_level["job_title"].str.contains("data", case=False, na=False)]
        ml_jobs = df_level[df_level["job_title"].str.contains("machine learning|ML", case=False, na=False)]
        ai_jobs = df_level[df_level["job_title"].str.contains("intelligence|AI", case=False, na=False)]
        software_jobs = df_level[df_level["job_title"].str.contains("software|developer", case=False, na=False)]

        # Combine indices
        main_indices = data_jobs.index.union(ml_jobs.index).union(ai_jobs.index).union(software_jobs.index)
        other = df_level.loc[~df_level.index.isin(main_indices)]

        # Count jobs
        job_counts = {
            "Data Analyst": len(data_jobs),
            "Machine Learning": len(ml_jobs),
            "Artificial Intelligence": len(ai_jobs),
            "Software Engineering": len(software_jobs),
            "Other": len(other)
        }

        # Generate pie chart
        plt.figure(figsize=(9, 9))
        plt.pie(
            job_counts.values(),
            labels=job_counts.keys(),
            autopct="%1.1f%%",
            startangle=90,
            colors=["lightcoral", "skyblue", "lightgreen", "gold", "lightgray"],
            explode=[0.05]*len(job_counts),
            textprops={'fontsize': 15}
        )
        plt.title(f"{job_levels[level]} Job Title Distribution by Category", fontsize=18)
        plt.tight_layout()

        print(f"\nThe pie chart for Job Title Distribution by Category in {job_levels[level]} are generated!")

        
        filename = f"/{directory}/{level}_demanding_job_pie.png"
        plt.savefig(filename, dpi=300)
        print(f"\nThe figure is saved in {filename}.\n")
        time.sleep(1)
        
        
        figures.append({
                    "filename": filename,
                    "section": f"{job_levels[level]} Job Distribution",
                    "title": f"{job_levels[level]} Job Title Distribution by Category",
                    "caption": f"The pie chart shows the distribution of full-time {job_levels[level]} positions across five categories: Data Analysis, Machine Learning, Artificial Intelligence, Software Engineering, and Other. Titles were systematically categorized using keyword matching: roles containing “data” were grouped as Data Analyst positions; titles with “machine learning” or “ML” were classified as Machine Learning; those containing “intelligence” or “AI” were assigned to Artificial Intelligence; and titles featuring “software” or “developer” were categorized as Software Engineering. Any remaining entries were placed into an Other category."
                })

    print("-------------End of 1------------\n")
    return figures

#2
def job_cat_salary(df, directory):
    '''
    Show bar graph of the salaries of Job Title by Category for your job level of interest.
    Entry level = EN
    Mid level = MI
    Senior level = SE
    Executive/director level = EX
    '''

    print("-------------2-------------")
    print("Compare the salary of Job Title by Category specified experience levels...")
    print("-------------2-------------")
    time.sleep(2)
    print("\nPlease specify which experience levels you are more interested in:")
    time.sleep(1)
    for code, desc in job_levels.items():
        print(f"{desc} = {code}")

    # Ask for multiple selections, comma-separated
    levels_input = input(
        "\nPlease select your job level(s) of interest (comma-separated, e.g., EN,MI,SE). Feel free to choose all of them: "
    ).strip().upper()

    # Split input into list and clean spaces
    selected_levels = [lvl.strip() for lvl in levels_input.split(",") if lvl.strip() in job_levels]

    if not selected_levels:
        print("No valid job levels entered. Please enter EN, MI, SE, or EX.")
        sys.exit()
    
    figures = []
    for level in selected_levels:
        df_level = df[df["experience_level"] == level]

        # Categorize jobs
        data_jobs = df_level[df_level["job_title"].str.contains("data", case=False, na=False)]
        ml_jobs = df_level[df_level["job_title"].str.contains("machine learning|ML", case=False, na=False)]
        ai_jobs = df_level[df_level["job_title"].str.contains("intelligence|AI", case=False, na=False)]
        software_jobs = df_level[df_level["job_title"].str.contains("software|developer", case=False, na=False)]

        # Combine indices
        main_indices = data_jobs.index.union(ml_jobs.index).union(ai_jobs.index).union(software_jobs.index)
        other = df_level.loc[~df_level.index.isin(main_indices)]

        job_en = {
            "Data Analyst": data_jobs,
            "Machine Learning": ml_jobs,
            "Artificial Intelligence": ai_jobs,
            "Software Engineering": software_jobs,
            "Other": other
        }

        avg_sal=[]
        all_std=[]
        for key, job in job_en.items():
            salary = job["salary_in_usd"].mean() * 1.4
            std = job["salary_in_usd"].std() * 1.4
            avg_sal.append(salary)
            all_std.append(std)

        plt.figure(figsize=(12, 10))
        plt.bar(
            job_en.keys(),
            avg_sal,
            yerr=all_std,         # <-- error bars here
            capsize=5,                          # adds small horizontal line on each error bar
            color="gold",
            edgecolor="brown",
            alpha=0.9
        )

        plt.title(f"Average Salary of Job Title by Category {job_levels[level]} Jobs (Full-Time Only)", fontsize=18)
        plt.xlabel("Job Categories", fontsize=15)
        plt.ylabel("Average Salary (CAD$)", fontsize=15)
        plt.xticks(fontsize=12) 
        plt.yticks(fontsize=12)  
        plt.grid(axis="y", linestyle="--", alpha=0.6)

        # Add data labels above bars
        for i, avg in enumerate(avg_sal):
            plt.text(i, avg + 2000, f"${avg:,.0f}", ha="center", fontsize=13, color='brown')

        plt.tight_layout()

        print(f"The bar graph for Average Salary of Job Title by Category in {job_levels[level]} are generated!")

        filename = f"/{directory}/{level}_demanding_job_salary.png" 
        plt.savefig(filename, dpi=300)
        print(f"\nThe figure is saved in {filename}.\n")
        time.sleep(1)

            
        figures.append({
                "filename": filename,
                "section": f"{job_levels[level]} Salary Comparison",
                "title": f"{job_levels[level]} Job Salaries",
                "caption": "Bar chart comparing average salaries with standard deviation. The y-axis represents salary in Canadian dollars, and the x-axis lists job levels."
            })
    
    print("-------------End of 2-------------\n")
    return figures


def dic(df):
    en = df[df["experience_level"] == "EN"]
    mi = df[df["experience_level"] == "MI"]
    se = df[df["experience_level"] == "SE"]
    ex = df[df["experience_level"] == "EX"]

    levels_dict = {
        "Entry Level": en,
        "Mid Level": mi,
        "Senior Level": se,
        "Executive or Director": ex
    }

    return levels_dict

#3
def all_level_salary(df, directory):
    '''
    Show bar graph for the salaries of all experience levels.
    '''

    print("-------------3-------------")
    print("Overall salary distribution for all experience levels...")
    print("-------------3-------------")
    time.sleep(1)
    levels_dict = dic(df)

    # Compute average and standard deviation for each level
    avg_salaries = []
    std_salaries = []
    figures = []
    plt.figure(figsize=(12, 10))
    for key, level in levels_dict.items():
        avg = level["salary_in_usd"].mean() * 1.4
        std = level["salary_in_usd"].std() * 1.4
        avg_salaries.append(avg)
        std_salaries.append(std)

    # Salary plot with error bars
    plt.bar(
        levels_dict.keys(),
        avg_salaries,
        yerr=std_salaries,         # <-- error bars here
        capsize=5,                          # adds small horizontal line on each error bar
        color="skyblue",
        edgecolor="navy",
        alpha=0.9
    )

    plt.title("Average Salary by Experience Level (Full-Time Only)", fontsize=18)
    plt.xlabel("Experience Level", fontsize=15)
    plt.ylabel("Average Salary (CAD$)", fontsize=15)
    plt.xticks(fontsize=12) 
    plt.yticks(fontsize=12) 

    plt.grid(axis="y", linestyle="--", alpha=0.6)

    # Add data labels above bars
    for i, avg in enumerate(avg_salaries):
        plt.text(i, avg + 2000, f"${avg:,.0f}", ha="center", fontsize=13, color='navy')

    plt.tight_layout()

    print("The bar graph of Average Salary by Experience Level is generated!")
    
    filename = f"/{directory}/all_level_salary.png"
    plt.savefig(filename, dpi=300)
    print(f"\nThe figure is saved in {filename}.\n")
    time.sleep(1)
                
    figures.append({
        "filename": filename,
        "section": "Average Salary by Experience Level",
        "title": "Average Salary by Experience Level (Full-Time Only)",
        "caption": "Comparison of average salaries across all experience levels. The y-axis represents salary in Canadian dollars, and the x-axis lists job levels."
    })
    print("-------------End of 3-------------\n")
    return figures

#4
def count_job(df, directory):
    '''
    Show horizontal bar graph of self-reported job title distributions for specified experience levels.
    Entry level = EN
    Mid level = MI
    Senior level = SE
    Executive/director level = EX
    '''

    print("-------------4-------------")
    print("Visualize job title distributions for specified experience levels...")
    print("-------------4-------------")
    time.sleep(2)
    print("\nPlease specify which experience levels you are more interested in:")
    time.sleep(1)
    for code, desc in job_levels.items():
        print(f"{desc} = {code}")

    # Ask for multiple selections, comma-separated
    levels_input = input(
        "\nPlease select your job level(s) of interest (comma-separated, e.g., EN,MI,SE). Feel free to choose all of them: "
    ).strip().upper()

    # Split input into list and clean spaces
    selected_levels = [lvl.strip() for lvl in levels_input.split(",") if lvl.strip() in job_levels]

    if not selected_levels:
        print("No valid job levels entered. Please enter EN, MI, SE, or EX.")
        sys.exit()

    figures = []
    for level in selected_levels:
        df_level = df[df["experience_level"] == level]
    
        joben = df_level["job_title"].value_counts()
        job_counts = joben[joben > 30]
        #print(job_counts)

        # Bar plot
        plt.figure(figsize=(12, 10))
        plt.barh(job_counts.index, job_counts.values, color="lightcoral", alpha=0.8)
        plt.title(f"Number of Full-Time {job_levels[level]} Jobs by Job Title", fontsize=18)
        plt.xlabel("Number of Positions", fontsize=15)
        plt.ylabel("Job Title", fontsize=15)
        plt.xticks(fontsize=12) 
        plt.yticks(fontsize=12) 
        plt.grid(axis="x", linestyle="--", alpha=0.6)

        # Add counts on bars
        for i, v in enumerate(job_counts.values):
            plt.text(v + 0.3, i, str(v), va="center", fontsize=12)

        plt.tight_layout()

        print(f"The horizontal bar graph of Number of Full-Time {job_levels[level]} Jobs by Job Title is generated!")
        

        filename = f"/{directory}/{level}_job_title_distributions.png"
        plt.savefig(filename, dpi=300)
        print(f"\nThe figure is saved in {filename}.\n")
        time.sleep(1)
        
        figures.append({
                "filename": filename,
                "section": f"{job_levels[level]} Job Title Distribution",
                "title": f"Number of Full-Time {job_levels[level]} Jobs by Job Title",
                "caption": f"This horizontal bar graph shows the distribution of self-reported job titles with more than 30 entries in {job_levels[level]}. All job titles are self-reported by the professionals."
            })
        
        print("-------------End of 4------------\n")
        return figures

#5
def level_work_mode(df, directory):

    print("-------------5-------------")
    print("Analyze work mode (e.g. online, hybrid, on-site) distributions for all experience levels...")
    print("-------------5-------------")
    time.sleep(2)

    levels_dict = dic(df)

    labels = ["On Site", "Hybrid", "Remote"]
    colors = ["skyblue", "lightgreen", "lightcoral"]

    # Collect percentages for each level
    all_percentages = []

    for key, level in levels_dict.items():
        remote_counts = level["remote_ratio"].value_counts().sort_index()
        total = remote_counts.sum()
        percentages = [
            remote_counts.get(0, 0)/total*100,
            remote_counts.get(50, 0)/total*100,
            remote_counts.get(100, 0)/total*100
        ]
        all_percentages.append(percentages)

    # Convert to numpy array for easier plotting (shape: 4x3 → 3x4 for stacking)
    all_percentages = np.array(all_percentages).T  # shape: 3 x 4 (0%,50%,100%)

    # Plot horizontal stacked bars
    fig, ax = plt.subplots(figsize=(10,6))
    levels = list(levels_dict.keys())
    left = np.zeros(len(levels))

    figures = []
    for i in range(len(labels)):
        ax.barh(levels, all_percentages[i], left=left, color=colors[i], label=labels[i], height=0.7)
        # Add percentage labels in the middle of each stack
        for j in range(len(levels)):
            if all_percentages[i][j] > 0:
                ax.text(left[j] + all_percentages[i][j]/2, j, f"{all_percentages[i][j]:.1f}%", 
                        ha='center', va='center', color='black', fontsize=9)
        left += all_percentages[i]

    ax.set_xlabel("Percentage of Jobs (%)")
    ax.set_title("Remote Work Distribution by Experience Level (Full-Time)", fontsize=15)
    ax.legend(title="Work mode", loc="upper left", bbox_to_anchor=(1, 1))
    plt.grid(axis="x", linestyle="--", alpha=0.6)
    plt.tight_layout()

    print("The stacked bar graph of Remote Work Distribution by Experience Level (Full-Time) is generated!")

    filename = f"/{directory}/all_level_work_mode.png"
    plt.savefig(filename, dpi=300)
    print(f"\nThe figure is saved in {filename}.\n")
    time.sleep(1)

    figures.append({
        "filename": filename,
        "section": "Work Mode Analysis",
        "title": "Bar graph of work arrangement prevalence",
        "caption": "The proportion of positions in onsite (blue), hybrid (green), and fully remote (red) work modes is shown across the four seniority levels. The y-axis represents job seniority, and the x-axis indicates the percentage of positions. Onsite work dominates across all levels, hybrid roles are rare, and remote work increases with seniority, peaking at senior-level positions."
    })
    print("-------------End of 5-------------\n")
    return figures
    



def generate_report(selected_options, filepath):
    '''
    Generate pdf or latex report with all the graphs amd figure captions for specified analysis.
    
    :param selected_options: all the graphs and figure captions
    :param filepath: the report will be stored at the same places with all the graphs
    '''

    if selected_options:
        report_type = input(
                    "Which type of report would you like to generate?\n"
                    "1 = LaTeX (.tex) only\n"
                    "2 = PDF (.pdf) only\n"
                    "3 = Both LaTeX and PDF\n"
                    "Enter 1, 2, or 3: "
                ).strip()

        if report_type not in {"1", "2", "3"}:
            print("No valid report type selected. Report not generated.")
            sys.exit()

        print("Generating report with selected figures...")

        tex_filename = f"{filepath}/salary_report.tex"
        pdf_filename = f"{filepath}/salary_report.pdf"

        title = input("Enter report title (Press Enter to use default): ").strip()
        if title == "":
            title = "Computer Science Job Market Report (2025)"

        margin = input("Enter page margin (e.g. 1in). Press Enter for default 1in: ").strip()
        if margin == "":
            margin = "1in"

        # ===== Write LaTeX =====
        with open(tex_filename, "w") as file:
            file.write(r"\documentclass{article}" + "\n")
            file.write(r"\usepackage[margin=" + margin + r"]{geometry}" + "\n")
            file.write(r"\usepackage{graphicx}" + "\n")
            file.write(r"\usepackage{float}" + "\n")
            file.write(r"\usepackage{caption}" + "\n")
            file.write(r"\begin{document}" + "\n\n")

            # Title
            file.write(r"\title{" + title + r"}" + "\n")
            file.write(r"\maketitle" + "\n\n")

            # Figures
            for item in selected_options:
                file.write(r"\section{" + item["section"] + r"}" + "\n")
                file.write(r"\begin{figure}[H]" + "\n")
                file.write(r"\centering" + "\n")
                file.write(
                    rf"\includegraphics[width=0.85\textwidth]{{{item['filename']}}}" + "\n"
                )
                file.write(
                    rf"\caption{{\textbf{{{item['title']}.}} {item['caption']}}}" + "\n"
                )
                file.write(r"\end{figure}" + "\n\n")

            # ===== Optional conclusion =====
            add_text = input("Would you like to add a custom conclusion? (Y/N): ").strip().upper()
            if add_text == "Y":
                user_text = input("Please enter your conclusion text:\n")
                file.write(r"\section{Conclusion}" + "\n")
                file.write(user_text + "\n\n")

            file.write(r"\end{document}")

        print(f"LaTeX file saved to: {tex_filename}")

        # ===== PDF generation =====
        if report_type in {"2", "3"}:
            print("please make sure you have downloaded pdflatext to proceed for PDF generation. If not, the pdf file will not be generated.")
            input("Press Enter to continue...")
            try:
                subprocess.run(
                    ["pdflatex", "-output-directory", filepath, tex_filename],
                    check=True
                )
                print(f"PDF report successfully generated at: {pdf_filename}")
            except Exception:
                print("PDF generation failed. Make sure pdflatex is installed.")



menu_options = {
    "1": ("Display the Job Title Distribution by Category in computer science in specified experience levels.", job_level_pie_chart),
    "2": ("Compare the salary of Job Title by Category in specified experience levels", job_cat_salary),
    "3": ("Overall salary distribution for all experience levels", all_level_salary),
    "4": ("Visualize job title distributions for specified experience levels", count_job),
    "5": ("Analyze work mode (e.g. online, hybrid, on-site) distributions for all experience levels", level_work_mode),
    "Q": ("Quit", None)
}


def main():

    print("\nThe following options are types of analyses we offer (Enter numbers or Q to quit):")
    for key, (desc, _) in menu_options.items():
        print(f"{key}. {desc}")

    choices = input("\nEnter your choices in a format like 1,3,5. If you only want to choose one option, just write a single number like 1: ").strip().upper().split(",")

    if len(choices) == 1 and choices[0] == "Q":
        print("Because you enter Q, we will exit the program for you.")
        sys.exit()
    
    directory = str(input("\nThank you for your choise. \n"
                            "Now, please give us the directory (folder) where your input file is located: "))
    selected_options = []

    for choice in choices:
        choice = choice.strip()

        if choice in menu_options:
            print("Leading to the graph generation interface...\n")
            _, func = menu_options[choice]
            
            if func:  
                time.sleep(1)
                while True:
                    try:
                        df = pd.read_csv(f"{directory}/Data Science, AI & ML Job Salaries in 2025.csv")
                        plot_info = func(df, directory)  # Run the function
                        selected_options.extend(plot_info)
                        break
                    except:
                        directory = input("Invalid directory. Re-enter your directory:")
                    
        else:
            print("Invalid choice. Please make sure your response is in the right format...")
            time.sleep(2)

    if selected_options:
        generate_report(selected_options, directory)
        print("Report generated successfully!")


if __name__ == "__main__":
    print("Hello! Welcome to ComSci Salary Explorer.\n")
    time.sleep(1)

    input("ComSci Salary Explorer is a python program designed to explore the 2025 computer science job market, discovering insights into salaries, job growth, and demand across the tech industry US and Canada.\n"
           "Press Enter to continue. Press Enter 6 times to skip introduction...\n")

    input("We focus on popular fields such as Data Science, Artificial Intelligence, and Machine Learning. Press Enter to continue...\n")

    input("Our reports include detailed graphs and charts to visualize the data clearly. Press Enter to continue...\n")

    input("You can filter results by job category, experience, or preferred technology stack. Press Enter to continue...\n")

    input("All insights are based on the latest 2025 self-reported data from computer science professionals on Kaggle. Press Enter to continue...\n")

    input("Ready to explore your career opportunities and potential earnings? Press Enter to continue...\n")

    print("Thank you! Let's get started! Do NOT press enter from now on.")
    time.sleep(2)

    main()






