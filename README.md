# 🤖 Medical Chatbot - AI Healthcare Assistant

An intelligent medical chatbot built with **Flask** backend and responsive **HTML/CSS/JavaScript** frontend. Get instant medical guidance and symptom analysis.

## ✨ Features

✅ **Real-time Medical Chatbot** - Get instant medical advice  
✅ **REST API Backend** - Flask-based scalable backend  
✅ **Interactive Frontend** - Beautiful HTML/CSS/JS interface  
✅ **Symptom Analysis** - Quick response for common symptoms  
✅ **CORS Enabled** - Cross-origin request support  
✅ **Environment Configuration** - Secure .env setup  
✅ **Error Handling** - Robust error management  
✅ **Responsive Design** - Works on all devices  

---

## 📁 Project Structure

ML-Medicals/
│
├── backend/
│ ├── app.py # Flask main application
│ ├── requirements.txt # Python dependencies
│ └── .env # Environment variables (local copy)
│
├── frontend/
│ └── index.html # Interactive chat UI
│
├── data/
│ ├── medical_knowledge_base.json # Medical data
│ └── training_data.json # Training dataset
│
├── .env # Main environment configuration
├── .gitignore # Git ignore rules
├── README.md # This file
│
└── chatbot.db # SQLite database (auto-created)

---

## 🚀 Installation

### **Prerequisites**
- Python 3.8+
- pip (Python package manager)
- Modern web browser
- Git (optional, for cloning)

### **Features Demonstrated:**
- ✅ Real-time message display
- ✅ Color-coded messages (blue for user, gray for bot)
- ✅ Multiple symptom testing
- ✅ Responsive input field
- ✅ Clean modern UI

---

## 🧪 Testing the Application

### **Test 1: Headache**

{
"response": "For headache, rest in dark room, hydrate, paracetamol 500mg every 6hrs. Consult doctor if persists >48hrs.",
"confidence": 0.95,
"message": "headache"
}

---

## 🛠️ Tech Stack

**Backend:**
- Flask 2.3.3
- Python 3.8+
- Flask-CORS 4.0.0
- SQLite3

**Frontend:**
- HTML5
- CSS3
- Vanilla JavaScript (ES6+)

**Version Control:**
- Git & GitHub

---

## 📈 Future Enhancements

- 🤖 Advanced NLP models
- 💾 User session history
- 🔐 User authentication
- 📊 Analytics dashboard
- 🌍 Multi-language support
- 📱 Mobile app
- 🗣️ Voice input/output
- 🧠 Personalized recommendations

---

## 👤 Author

**Tejaswini Hatakar**  
GitHub: [@tejaswinihatakar](https://github.com/tejaswinihatakar)  
Project: [ML-Medicals](https://github.com/tejaswinihatakar/ML-Medicals)

---

## 📄 License

MIT License - Feel free to use, modify, and distribute

---

## 🎯 Quick Commands

| Task | Command |
|------|---------|
| Start Backend | `cd backend && python app.py` |
| Open Frontend | `open frontend/index.html` |
| Test Headache | `curl -X POST http://127.0.0.1:5000/chat -H "Content-Type: application/json" -d '{"message": "headache"}'` |
| Install Deps | `pip install -r requirements.txt` |
| Check Status | `curl http://127.0.0.1:5000/` |

---

## ✅ Verification Checklist

- [ ] Backend running on http://127.0.0.1:5000
- [ ] Frontend opens in browser
- [ ] Can type in chat input
- [ ] Bot responds to symptoms
- [ ] All files on GitHub
- [ ] README visible on repo

---

**Happy chatting! 🎉 Your Medical Chatbot is ready to help!**

