<!--
Hey, thanks for using the awesome-readme-template template.  
If you have any enhancements, then fork this project and create a pull request 
or just open an issue with the label "enhancement".

Don't forget to give this project a star for additional support ;)
Maybe you can mention me or this repo in the acknowledgements too
-->

<div align="center">

  <img src="https://res.cloudinary.com/dtobcdrww/image/upload/v1740831156/Screenshot_2025-03-01_171255_d4t58v.png" alt="logo" width="auto" height="auto" />
  <h1></h1>
<p>
ScamShield is an intelligent platform designed to detect suspicious calls and prevent fraud by analyzing call recordings using advanced AI techniques.
</p>
<p>
By leveraging state-of-the-art speech-to-text models and custom-trained natural language processing algorithms, ScamShield transforms audio into actionable insights. It identifies key indicators—such as urgent language, requests for sensitive information, and common social engineering cues—to flag potentially fraudulent calls in real time.
</p>
<p>
The platform seamlessly preprocesses and normalizes diverse audio data, ensuring accurate transcription and robust classification. With its intuitive dashboard and comprehensive reporting, ScamShield empowers users, financial institutions, and organizations to make data-driven decisions and safeguard against fraud.
</p>

   
</div>

<br />

<!-- Table of Contents -->
# :notebook_with_decorative_cover: Table of Contents

- [About the Project](#star2-about-the-project)
  * [Screenshots](#camera-screenshots)
  * [Tech Stack](#space_invader-tech-stack)
  * [Features](#dart-features)
- [Getting Started](#toolbox-getting-started)
  * [Run Locally](#running-run-locally)
- [Roadmap](#compass-roadmap)
- [Feature Scope](#feature-scope)
- [Improvements](#improvements)
  

<!-- About the Project -->
## :star2: About the Project


<!-- Screenshots -->
### :camera: Screenshots

<div align="center"> 
  <img src="https://res.cloudinary.com/dtobcdrww/image/upload/v1740831359/Screenshot_2025-03-01_171337_h7tk7y.png" alt="screenshot" />
</div>
<div align="center"> 
  <img src="https://res.cloudinary.com/dtobcdrww/image/upload/v1740831128/Screenshot_2025-03-01_172032_hlyy3q.png" alt="screenshot" />
</div>
<div align="center"> 
  <img src="https://res.cloudinary.com/dtobcdrww/image/upload/v1740831372/Screenshot_2025-03-01_172007_cvl6qt.png" alt="screenshot" />
</div>
<div align="center"> 
  <img src="https://res.cloudinary.com/dtobcdrww/image/upload/v1740831401/Screenshot_2025-03-01_171315_vd5ass.png" alt="screenshot" />
</div>


<!-- TechStack -->
### :space_invader: Tech Stack

<details>
  <summary>Client</summary>
  <ul>
    <li><a href="https://reactjs.org/">React.js</a></li>
    <li><a href="https://tailwindcss.com/">TailwindCSS</a></li>
  </ul>
</details>

<details>
  <summary>Server</summary>
  <ul>
    <li><a href="https://www.python.org/">Python</a></li>
    <li><a href="https://flask.palletsprojects.com/en/stable/">Flask</a></li>
    <li><a href="https://openai.com/index/whisper/">Open AI Whisper</a></li>
    <li><a href="https://librosa.org/doc/latest/index.html">Librosa</a></li>
     <li><a href="https://ai.google.dev/gemini-api/docs/api-key">Gemini Generative API</a></li>
    <li><a href="https://scikit-learn.org/">scikit-learn</a></li>
    <li><a href="https://www.nltk.org/">NLTK</a></li>
  </ul>
</details>

<details>
  <summary>Storage</summary>
  <ul>
    <li><a href="https://drive.google.com/file/d/1zjUoLHDVdHR84MVzdz8-1kVP0qq5q883/view?usp=sharing">Dataset of Transcripts</a></li>
  </ul>
</details>


<!-- Features -->
### :dart: Features

<details>
  <summary>🎯 Features</summary>
  <ul>
    <li>🎤 Real-Time Audio Transcription: Converts call recordings to text accurately and efficiently.</li>
    <li>🛡️ Suspicious Call Detection: Uses advanced AI algorithms to flag potentially fraudulent or suspicious calls.</li>
    <li>🧹 Robust Audio Preprocessing: Filters out background noise to enhance speech clarity and transcription quality.</li>
    <li>🔍 Comprehensive Analysis: Highlights key risk indicators such as urgent language, OTP requests, and social engineering cues.</li>
    <li>📊 Detailed Reporting & Analytics: Provides actionable insights with risk assessments and interactive dashboards.</li>
    <li>💡 Explainability: Offers transparent explanations on why a call was flagged, aiding in decision-making and trust.</li>
    <li>🔒 Secure & Compliant: Ensures data privacy and secure handling of sensitive audio and transcription data.</li>
  </ul>
</details>


<!-- Getting Started -->
## 	:toolbox: Getting Started

<!-- Prerequisites -->
### :bangbang: Prerequisites

This project uses npm as package manager

```bash
 npm install 
```

<!-- Run Locally -->
### :running: Run Locally


Clone the project

```bash
  git clone https://github.com/Shivagad/ScamScamShieldA.git
```
### :computer: Client

Go to the project directory

```bash
  cd Frontend
```

Install dependencies

```bash
  npm install
```

Start the Client

```bash
  npm run dev
```

### :computer: Server

Go to the project directory

```bash
  cd Backend
```

Install dependencies

```bash
  pip install requirements.txt
```

Start the Server

```bash
  python index.py
```

<!-- Roadmap -->
## 🧭 Roadmap

* [x] Set up project structure and initial configurations  
* [x] Implement secure user authentication and authorization (JWT-based)  
* [x] Develop and integrate robust audio preprocessing (noise reduction, normalization)  
* [x] Integrate speech-to-text transcription using advanced models (e.g., Whisper)  
* [x] Train and fine-tune the classification model to detect suspicious calls  
* [x] Implement explainability features (e.g., LIME/SHAP, attention visualization) to detail decision factors  
* [x] Design an interactive dashboard for real-time call monitoring and comprehensive reporting  
* [x] Establish real-time alert mechanisms for flagged suspicious calls  
* [ ] Enhance UI/UX for a seamless and intuitive user experience (React, Tailwind CSS)  
* [ ] Optimize model performance to reduce latency in real-time processing  
* [ ] Implement multi-language support for diverse audio inputs (e.g., Hindi, Marathi)  
* [ ] Develop a mobile-responsive interface for on-the-go monitoring and alerts  

## Feature Scope

ScamShield is an advanced fraud detection platform designed to protect users from suspicious calls by leveraging cutting-edge AI-driven audio analysis. The current scope of features includes:

- **Real-Time Audio Transcription:**  
  Converts call recordings into text using state-of-the-art models (e.g., Whisper) for accurate transcription, even in noisy environments.

- **Robust Audio Preprocessing:**  
  Employs advanced noise reduction and normalization techniques to enhance speech clarity and ensure reliable transcription.

- **Suspicious Call Detection:**  
  Uses a fine-tuned classification model to analyze transcribed text for key indicators of fraud, such as urgent language, OTP requests, and social engineering cues.

- **Explainability and Transparency:**  
  Integrates post-hoc explainability tools (e.g., LIME/SHAP, attention visualization) to highlight the factors contributing to a call being flagged, thereby building user trust.

- **Interactive Analytics Dashboard:**  
  Provides comprehensive, real-time insights including risk assessments, detailed reports, and instant alerts, all accessible via an intuitive web-based interface.

- **Secure User Authentication:**  
  Implements JWT-based authentication to ensure that only authorized users can access sensitive call data and analytics.

- **Multi-Language Support:**  
  Capable of processing audio in multiple languages (e.g., Hindi, Marathi) with ongoing improvements to expand language accuracy and coverage.

## Improvements

Planned enhancements and future directions for ScamShield include:

- **Enhanced User Interface and Experience:**  
  Redesign the dashboard with modern front-end frameworks (e.g., React, Tailwind CSS) for a more intuitive, responsive, and visually appealing user experience.

- **Optimized Real-Time Processing:**  
  Improve the efficiency of audio processing and transcription to reduce latency, ensuring faster detection and alerting of suspicious calls.

- **Advanced Classification Models:**  
  Explore end-to-end audio classification and additional deep learning architectures to further boost detection accuracy and capture subtle fraud indicators.

- **Refined Explainability:**  
  Develop more granular and user-friendly explainability features to provide detailed insights into why specific calls are flagged, helping users make informed decisions.

- **Expanded Language and Dialect Coverage:**  
  Broaden the range of supported languages and regional dialects to better serve a diverse, global user base.

- **Mobile Responsiveness and App Development:**  
  Create a mobile-responsive interface or dedicated mobile app to allow users to monitor and receive alerts on the go.

- **Integration with Additional Data Sources:**  
  Incorporate supplementary data streams such as call metadata, user behavior analytics, and contextual information to enrich fraud detection capabilities.

- **Continuous Learning Feedback Loop:**  
  Implement a system to gather user feedback and real-world performance data, enabling continuous model refinement and reduction of false positives.

These improvements aim to make ScamShield not only more accurate and efficient but also more user-centric, ensuring a seamless, secure, and comprehensive solution for fraud detection in call communications.
