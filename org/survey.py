import matplotlib.pyplot as plt

# Function to plot each question
def plot_question(data, title, years, ax):
    ax.plot(years, data, marker='o')
    ax.set_title(title)
    ax.set_xlabel('Year')
    ax.set_ylabel('Percentage (%)')
    ax.set_xticks(years)
    ax.grid(True)

# Updated data for the questions with 2024 included
years = [2019, 2020, 2021, 2022, 2023, 2024]
q1_data = [39, 26, 18, 20, 30.8, 36.2]
q2_data = [52, 30, 28, 35, 66.6, 52.8]
q3_data = [73, 50, 44, 44, 57.9, 41.7]  # Updated with consistent 2022 data
q4_data = [11, 17, 14, 21, 17.9, 13.9]
q5_data = [8, 13, 19, 18, 12.9, 13.9]
q6_data = [8, 17, 31, 12, 25.7, 30.5]
q7_data = [77, 78, 80, 85, 73.7, 80.6]
q8_data = [28, 53, 47, 56, 43.6, 33.3]

# Plotting
fig, axes = plt.subplots(4, 2, figsize=(15, 20))
fig.subplots_adjust(hspace=0.5)

plt.clf()
plot_question(q1_data, "Optimism about the future of the College", years, axes[0, 0])
plot_question(q2_data, "Confidence in the leadership of the College", years, axes[0, 1])
plot_question(q3_data, "Confidence in quality academic experience", years, axes[1, 0])
plot_question(q4_data, "Adequacy of compensation", years, axes[1, 1])
plot_question(q5_data, "Compensation commensurate to contributions", years, axes[2, 0])
plot_question(q6_data, "Support to achieve teacher/scholar model", years, axes[2, 1])
plot_question(q7_data, "Professional fulfillment from teaching", years, axes[3, 0])
plot_question(q8_data, "Primary professional stressor: Solvency of the College", years, axes[3, 1])

#plt.show()
plt.savefig("survey.png")
