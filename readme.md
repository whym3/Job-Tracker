# Job Application Tracker

![Job Tracker Banner](https://via.placeholder.com/1000x300.png?text=Job+Application+Tracker)

## 📌 Overview
The **Job Application Tracker** is a Python-based tool that helps users log their job applications into **Google Sheets** effortlessly. It provides an interactive command-line interface to record company names, job positions, statuses, and notes, ensuring better organization and tracking of your job search progress.

## ✨ Features
- 📝 **Easy Data Entry**: Prompt-based input system for job applications.
- 🔗 **Google Sheets Integration**: Automatically saves job details to Google Sheets.
- 🔄 **Status Tracking**: Keep track of applications with statuses like "Applied" or "Rejected".
- ⏳ **Continuous Entry Mode**: Add multiple applications without restarting the program.
- ✅ **Error Handling**: Prevents empty inputs and handles API errors gracefully.

## 🚀 Setup Instructions
### 1️⃣ Prerequisites
Ensure you have the following installed:
- Python (>= 3.7)
- Google API Client Libraries
- A **Google Cloud Project** with a Service Account

### 2️⃣ Install Required Packages
Run the following command to install dependencies:
```sh
pip install google-api-python-client google-auth google-auth-oauthlib google-auth-httplib2
```

### 3️⃣ Configure Google Sheets API
1. Go to **Google Cloud Console**.
2. Create a **Service Account** and download the JSON credentials file.
3. Share your Google Sheet with the service account's email.
4. Replace `SERVICE_ACCOUNT_FILE` in `job_tracker_sheets.py` with your credentials file path.
5. Update `SHEET_ID` and `SHEET_NAME` with your Google Sheet details.

## 🛠 Usage
Run the script using:
```sh
python job_tracker_sheets.py
```
Follow the prompts to enter job details and save them to your Google Sheet.

## 📌 Example Output
```sh
Enter company name: Google
Enter position title: Software Engineer
Select application status:
1. Applied
2. Rejected
Enter the number corresponding to the status: 1
Enter any notes (optional): Referred by a friend
Application details saved to Google Sheets.
```

## ⚠ Troubleshooting
### "ModuleNotFoundError: No module named 'googleapiclient'"
Run:
```sh
pip install google-api-python-client
```
### "Permission Denied in Google Sheets"
Ensure your service account email has **edit access** to the spreadsheet.

## 📜 License
This project is licensed under the **MIT License**.

## 🙌 Contributing
Feel free to fork this repository, improve the script, and submit pull requests.

## 📞 Contact
For any issues or suggestions, reach out via [GitHub Issues](https://github.com/your-repo/issues).

