# MITRE_Groups_Overlap_Project

# MITRE Groups Overlap Project

A Python tool to measure the similarity between threat actor groups based on the MITRE ATT&CK techniques they use.

---

## 🔍 Overview

This script retrieves data from the MITRE ATT&CK website, analyzes the attack techniques used by different groups, and calculates overlap percentages. It then generates:

- A detailed comparison report (screen + output file)
- A separate list of group pairs with ≥85% similarity (for the group with fewer techniques)

---

## 📋 Features

- **Pairwise or bulk comparison**:  
  - Compare specific groups you choose  
  - Automatically compare all groups in the dataset

- **Outputs include**:  
  - Percent overlap  
  - Common techniques  
  - Unique techniques  
  - List of high-similarity group pairs (≥85% threshold)

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.9+**  
- Libraries:
  - `pandas`
  - `requests`
  - `beautifulsoup4`
  - `json`
  - `os`

Install them via:

```bash
pip install pandas requests beautifulsoup4
```

---

### 🧰 Installation

1. Clone this repository:
    ```bash
    git clone https://github.com/cyghtinc/MITRE_Groups_Overlap_Project.git
    cd MITRE_Groups_Overlap_Project
    ```
2. Ensure dependencies are installed (see prerequisites).

---

## ⚙️ Usage

Run the main script:

```bash
python compare_groups.py
```

You'll be prompted to choose:

1. **Specific groups** – enter group names (from the included `Groups` file or MITRE ATT&CK)  
2. **All groups** – automatically compare every group available

### Outputs

- **Comparison results**: shown in console and saved as `output_<timestamp>.json`  
- **High similarity report**: `high_similarity_pairs_<timestamp>.json` (≥85%)

---

## 🛠️ Example

1. Choose option 1 and enter:
   ```
   APT28, FIN7
   ```
2. Output shows:
   - % overlap  
   - List of shared techniques  
   - Unique techniques for each group  
3. If similarity ≥85%, it's saved in the high-similarity report.

---

## 📅 Configuration

You can customize:

- Similarity threshold (default: 85%) – change at top of script
- Output directory – adjust in `compare_groups.py`
- Input groups list – edit the provided `Groups` file

---

## ❓ Troubleshooting

- **MITRE website downtime**: script may fail to download data  
- **Missing libraries**: install via `pip install …`  
- **Unique file names**: timestamps prevent overwriting

---

## 📝 Contributing

Feel free to submit issues or PRs—happy to improve:

- Add CLI arguments  
- Support more output formats  
- Parallelize large comparisons

---

## 📄 License

This project is released under the **MIT License**.

---

## 📧 Contact

For questions or feedback, reach out to the author at `your-email@example.com`.





Explanation Summary:
The script compares all the groups according to the attack techniques each group works with.
The script goes to MITRE ATTACK website and downloads the relevant information of all groups, performs a comparison according to the attack techniques and finally shows the percentages that the groups were identical, the identical techniques and also the different techniques. The information is displayed as output to the screen as well as to a file. In addition, a file of all the groups we identified had a similarity of 85% or more between their attack techniques is created.
The percentage of similarity is determined in relation to the group that uses a smaller amount of techniques.

The user can choose between 2 options:
1. Comparison between specific groups which he wants to compare - the groups can be found in the attached file called Groups or he can find the groups on the MITER ATTACK website.
2. The script will automatically compare all groups.

Requirements for running the script:
Python version: 3.9 or higher.
Required libraries: PANDAS, requests, beautifulsoup from bs4, json, os.
