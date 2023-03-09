# MITRE_Groups_Overlap_Project
Explanation:
The script compares all the groups according to the attack techniques each group works with.
The script goes to MITER ATTACK website and downloads the relevant information of all groups, performs a comparison according to the attack techniques and finally shows the percentages that the groups were identical, the identical techniques and also the different techniques. The information is displayed as output to the screen as well as to a file. In addition, a file of all the groups we identified had a similarity of 85% or more between their attack techniques is created.
The percentage of similarity is determined in relation to the group that uses a smaller amount of techniques.

The user can choose between 2 options:
1. Comparison between specific groups which he wants to compare - the groups can be found in the attached file called Groups or he can find the groups on the MITER ATTACK website.
2. The script will automatically compare all groups.

Requirements for running the script:
Python version: 3.9 or higher.
Required libraries: PANDAS, requests, beautifulsoup from bs4, json, os.
