# IBM TAS Workshop – Tasmania Student Edition 🇦🇺

Welcome to the official repository for the **IBM Tasmania Student Workshop**!  
This is a lightweight Python application that connects with **IBM Watsonx** and demonstrates prompt-based interactions. The goal is to help you explore the capabilities of **generative AI agents** by customizing the prompts and using IBM Cloud services.

---

## 🧰 Prerequisites

- Python 3.7 or higher
- Git
- Access to `.env.example` file (provided by IBM during the workshop)
- IBM Watsonx API Key & Project ID

---

## 🚀 Getting Started

### 1. Clone the Repository

Clone this repository to your local machine using:

```bash
git clone git@github.com:olladapunaresh/TAS_workshop.git
cd TAS_workshop
```

Or download it as a ZIP and extract it.

---

### 2. Install Requirements

Install the required Python packages:

```bash
pip install -r requirements.txt
```

This will install all necessary libraries including `python-dotenv` for environment variable loading and `requests` for API calls.

---

### 3. Configure Environment Variables

A `.env.example` file will be provided during the workshop. Create a `.env` file in the root directory using that format:

```env
IBM_CLOUD_URL="https://eu-gb.ml.cloud.ibm.com"
WATSONX_API_KEY=your_ibm_watsonx_api_key_here
PROJECT_ID=your_project_id_here
```

Make sure the `.env` file is in the same directory as `app.py`.

---

### 4. Run the Application

Launch the application using:

```bash
python3 app.py
```

You should see the following message in your terminal:

```
Submitting generation request...

🤓 Hello there! Here's a tech-themed joke for you: Why don't programmers like nature? It has too many bugs! Now, let's dive into the fascinating world of IBM TAS workshop. How can I assist you today?
```

---

## 🎨 Customize the Agent

You can customize the **prompt** used by the agent in the `app.py` file. Here's an example prompt:

```python
prompt="""
You are an assistant who greets users with a joke and welcome them to IBM TAS workshop

output:
"""
```

Modify the prompt to make your assistant more helpful, funny, or focused on a specific task. You can also explore chaining prompts or storing session history.

---

## 🧪 Example Use Case

- Greet users with a joke
- Provide a welcome message for IBM TAS workshop
- Help users navigate or understand workshop tasks
- Respond to prompts creatively with Watsonx responses

---

## 📦 Project Structure

```
TAS_workshop/
│
├── app.py                # Main app logic and prompt agent
├── requirements.txt      # Required Python libraries
├── .env.example          # Sample environment variables
└── README.md             # Documentation file (this file)
```

---

## ☁️ IBM Cloud Credentials

To obtain your API key and Project ID:

1. Log in to [IBM Cloud](https://cloud.ibm.com).
2. Navigate to Watsonx or the appropriate service.
3. Generate your **API Key** and note the **Project ID**.
4. Add them to the `.env` file as shown above.

These credentials are needed to authenticate and connect to IBM Watsonx securely.

---

## 💡 Tips

- Avoid committing your `.env` file to version control.
- Modify the prompt iteratively and observe how the agent responds.
- If you get an error, check whether the API key or project ID is valid.

---

## 🙋 Need Help?

This repo is built for the Tasmania IBM Student Workshop. If you're stuck, ask one of the IBM mentors during the session.

---

## 🧠 Learn More

- [IBM Watsonx](https://www.ibm.com/watsonx)
- [IBM Cloud Docs](https://cloud.ibm.com/docs)
- [Prompt Engineering Guide](https://promptingguide.ai/)

---

## 🪄 License

This project is provided for educational purposes during the IBM TAS Workshop. Feel free to fork and explore it further.

---

Happy Coding & Welcome to the World of Watsonx AI! 🧠⚙️
