import React, { useState, useRef } from 'react';
import { motion } from 'framer-motion';
import { Canvas } from '@react-three/fiber';
import { OrbitControls, Sphere } from '@react-three/drei';
import {
  ShieldCheckIcon,
  BoltIcon,
  ChartBarIcon,
  PhoneIcon,
  ExclamationTriangleIcon,
  DocumentCheckIcon,
  XMarkIcon
} from '@heroicons/react/24/outline';

function FloatingSphere() {
  return (
    <Sphere args={[1, 32, 32]}>
      <meshStandardMaterial color="#0ea5e9" wireframe />
    </Sphere>
  );
}

const features = [
  {
    icon: ShieldCheckIcon,
    title: "Advanced Protection",
    description: "Our AI-powered system analyzes call patterns and linguistic markers to identify potential scams."
  },
  {
    icon: BoltIcon,
    title: "Real-Time Analysis",
    description: "Get instant feedback on suspicious calls with our state-of-the-art ML model."
  },
  {
    icon: ChartBarIcon,
    title: "Detailed Reports",
    description: "Receive comprehensive analysis report with risk assessment and recommendations."
  }
];

const workflowSteps = [
  {
    icon: PhoneIcon,
    title: "Record Call",
    description: "Record or save the suspicious call you want to analyze"
  },
  {
    icon: DocumentCheckIcon,
    title: "Upload Audio",
    description: "Upload the recorded call to our secure platform"
  },
  {
    icon: BoltIcon,
    title: "AI Analysis",
    description: "Our ML model analyzes the call for scam patterns"
  },
  {
    icon: ExclamationTriangleIcon,
    title: "Get Results",
    description: "Receive detailed analysis and risk assessment"
  }
];

function App() {
  const [audioFile, setAudioFile] = useState(null);
  const [recordedAudio, setRecordedAudio] = useState(null);
  const [analysis, setAnalysis] = useState(null);
  const [isAnalyzing, setIsAnalyzing] = useState(false);

  const fileInputRef = useRef(null);
  const uploadSectionRef = useRef(null);

  // Refs for recording
  const [isRecording, setIsRecording] = useState(false);
  const mediaRecorderRef = useRef(null);
  const audioChunksRef = useRef([]);

  const handleFileChange = (e) => {
    const file = e.target.files[0];
    if (file && file.type.includes('audio')) {
      setAudioFile(file);
      // Clear any previous recording if present
      setRecordedAudio(null);
    }
  };

  const handleGetStarted = () => {
    uploadSectionRef.current?.scrollIntoView({ behavior: 'smooth' });
  };

  // Analyze either the uploaded file or recorded audio
  const handleSubmit = async (fileToAnalyze) => {
    if (!fileToAnalyze) return;
    setIsAnalyzing(true);
    const formData = new FormData();
    formData.append('file', fileToAnalyze);
    try {
      const response = await fetch('http://localhost:5000/predict', {
        method: 'POST',
        body: formData
      });
      const result = await response.json();
      setAnalysis({
        riskLevel: result.prediction === "Fraud" ? "Suspicious Call" : "Not a Suspicious Call",
        confidence: "N/A", // Update if backend provides confidence
        suspiciousPatterns: [],
        transcript: result.transcription || "",
        gemini_analysis:result.gemini_analysis || ""
      });
    } catch (error) {
      console.error("Error during analysis:", error);
    }
    setIsAnalyzing(false);
  };

  const handleAnalyzeUploaded = () => {
    handleSubmit(audioFile);
  };

  const handleAnalyzeRecording = () => {
    // Convert recorded blob to File before analysis
    const file = new File([recordedAudio], "recording.mp3", { type: 'audio/mp3' });
    handleSubmit(file);
  };

  // Recording functionality using MediaRecorder API
  const handleStartRecording = async () => {
    try {
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
      const options = { mimeType: 'audio/mp3' };
      try {
        mediaRecorderRef.current = new MediaRecorder(stream, options);
      } catch (e) {
        console.warn("audio/mp3 not supported, falling back to default", e);
        mediaRecorderRef.current = new MediaRecorder(stream);
      }
      audioChunksRef.current = [];
      mediaRecorderRef.current.ondataavailable = event => {
        if (event.data.size > 0) {
          audioChunksRef.current.push(event.data);
        }
      };
      mediaRecorderRef.current.onstop = () => {
        const audioBlob = new Blob(audioChunksRef.current, { type: 'audio/mp3' });
        setRecordedAudio(audioBlob);
        // Clear any uploaded file if present
        setAudioFile(null);
      };
      mediaRecorderRef.current.start();
      setIsRecording(true);
    } catch (error) {
      console.error("Error accessing microphone:", error);
    }
  };

  const handleStopRecording = () => {
    if (mediaRecorderRef.current) {
      mediaRecorderRef.current.stop();
      setIsRecording(false);
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-primary-900 to-primary-700 text-white">
      {/* Hero Section */}
      <section className="relative h-screen flex items-center">
        <div className="absolute inset-0 overflow-hidden">
          <Canvas className="w-full h-full">
            <ambientLight intensity={0.5} />
            <pointLight position={[10, 10, 10]} />
            <OrbitControls enableZoom={false} autoRotate />
            <FloatingSphere />
          </Canvas>
        </div>
        
        <div className="container mx-auto px-6 relative z-10">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.8 }}
            className="text-center"
          >
            <h1 className="text-6xl font-bold mb-6">ScamSheild AI</h1>
            <p className="text-xl mb-8 max-w-2xl mx-auto">
              Protect yourself from fraudulent calls using our advanced AI-powered analysis. 
              Upload your call recordings or record directly in your browser, and let our ML model identify potential scam attempts.
            </p>
            <div className="flex justify-center gap-4">
              <motion.button
                onClick={handleGetStarted}
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                className="bg-primary-500 px-8 py-3 rounded-lg font-semibold hover:bg-primary-400"
              >
                Get Started
              </motion.button>
            </div>
          </motion.div>
        </div>
      </section>

      {/* Purpose Section */}
      <section className="py-20 bg-primary-800/50 backdrop-blur-lg">
        <div className="container mx-auto px-6">
          <motion.div
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            className="text-center max-w-4xl mx-auto"
          >
            <h2 className="text-4xl font-bold mb-6">Why ScamShield?</h2>
            <p className="text-lg mb-12 text-primary-100">
              In today's digital age, phone scams have become increasingly sophisticated, 
              costing victims millions of dollars annually. ScamShield leverages cutting-edge 
              AI technology to protect you from these evolving threats.
            </p>
          </motion.div>
        </div>
      </section>

      {/* Features Section */}
      <section className="py-20">
        <div className="container mx-auto px-6">
          <h2 className="text-4xl font-bold text-center mb-12">Key Features</h2>
          <div className="grid md:grid-cols-3 gap-12">
            {features.map((feature, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ delay: index * 0.2 }}
                className="text-center"
              >
                <feature.icon className="h-12 w-12 mx-auto mb-4 text-primary-300" />
                <h3 className="text-xl font-semibold mb-2">{feature.title}</h3>
                <p className="text-primary-100/80">{feature.description}</p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Workflow Section */}
      <section className="py-20 bg-primary-800/50 backdrop-blur-lg">
        <div className="container mx-auto px-6">
          <h2 className="text-4xl font-bold text-center mb-12">How It Works</h2>
          <div className="grid md:grid-cols-4 gap-8">
            {workflowSteps.map((step, index) => (
              <motion.div
                key={index}
                initial={{ opacity: 0, y: 20 }}
                whileInView={{ opacity: 1, y: 0 }}
                transition={{ delay: index * 0.2 }}
                className="text-center relative"
              >
                {index < workflowSteps.length - 1 && (
                  <div className="hidden md:block absolute top-1/2 right-0 w-full h-0.5 bg-primary-600" />
                )}
                <div className="relative z-10">
                  <div className="bg-primary-700 rounded-full p-4 w-16 h-16 mx-auto mb-4 flex items-center justify-center">
                    <step.icon className="h-8 w-8 text-primary-300" />
                  </div>
                  <h3 className="text-xl font-semibold mb-2">{step.title}</h3>
                  <p className="text-primary-100/80">{step.description}</p>
                </div>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Upload / Record Section */}
      <section ref={uploadSectionRef} className="py-20 bg-primary-800/50 backdrop-blur-lg">
        <div className="container mx-auto px-6">
          <motion.div initial={{ opacity: 0 }} whileInView={{ opacity: 1 }} className="max-w-2xl mx-auto text-center">
            <h2 className="text-4xl font-bold mb-8">Analyze Your Call</h2>
            
            {/* File Upload Option */}
            <div className="space-y-6">
              <div
                onClick={() => fileInputRef.current?.click()}
                className="border-2 border-dashed border-primary-300 rounded-lg p-12 cursor-pointer hover:border-primary-200 transition-colors flex justify-between items-center"
              >
                <input
                  type="file"
                  ref={fileInputRef}
                  onChange={handleFileChange}
                  accept="audio/*"
                  className="hidden"
                />
                {audioFile ? (
                  <div className="flex items-center gap-2 w-full justify-between">
                    <span className="text-lg">{audioFile.name}</span>
                    <button onClick={(e) => { e.stopPropagation(); setAudioFile(null); }}>
                      <XMarkIcon className="h-5 w-5 text-red-500" />
                    </button>
                  </div>
                ) : (
                  <p className="text-lg">Click to upload audio file</p>
                )}
              </div>
              
              <motion.button
                whileHover={{ scale: 1.05 }}
                whileTap={{ scale: 0.95 }}
                onClick={handleAnalyzeUploaded}
                className="bg-primary-500 px-8 py-3 rounded-lg font-semibold hover:bg-primary-400 transition-colors flex items-center justify-center gap-2"
                disabled={!audioFile || isAnalyzing}
              >
                {isAnalyzing ? (
                  <div className="w-6 h-6 border-4 border-t-transparent border-white rounded-full animate-spin" />
                ) : "Analyze Recording"}
              </motion.button>
            </div>

            {/* Recording Option */}
            <div className="space-y-6 mt-12">
              <h3 className="text-2xl font-semibold">Or Record Audio</h3>
              {!isRecording ? (
                <button
                  onClick={handleStartRecording}
                  className="bg-primary-500 ml-10 px-8 py-3 rounded-lg font-semibold hover:bg-primary-400 transition-colors"
                >
                  Start Recording
                </button>
              ) : (
                <button
                  onClick={handleStopRecording}
                  className="bg-red-500 px-8 py-3 rounded-lg font-semibold hover:bg-red-400 transition-colors"
                >
                  Stop Recording
                </button>
              )}
              {recordedAudio && (
                <div className="mt-4 relative inline-block">
                  <audio controls src={URL.createObjectURL(recordedAudio)} className="w-full" />
                  <button 
                    onClick={() => setRecordedAudio(null)}
                    className="absolute top-0 right-0 bg-red-500 p-1 rounded-full"
                  >
                    <XMarkIcon className="h-4 w-4" />
                  </button>
                  <motion.button
                    whileHover={{ scale: 1.05 }}
                    whileTap={{ scale: 0.95 }}
                    onClick={handleAnalyzeRecording}
                    className="bg-primary-500 px-8 py-3 rounded-lg font-semibold hover:bg-primary-400 transition-colors mt-4 flex items-center justify-center gap-2"
                    disabled={isAnalyzing}
                  >
                    {isAnalyzing ? (
                      <div className="w-6 h-6 border-4 border-t-transparent border-white rounded-full animate-spin" />
                    ) : "Upload Recording"}
                  </motion.button>
                </div>
              )}
            </div>

            {/* Analysis Results */}
            {analysis && (
              <motion.div initial={{ opacity: 0, y: 20 }} animate={{ opacity: 1, y: 0 }} className="mt-12 bg-primary-800/50 backdrop-blur-lg p-6 rounded-lg">
                <h3 className="text-2xl font-bold mb-4">Analysis Results</h3>
                <div className="text-left">
                  <p className="mb-2">
                    Risk Level: <span className="text-red-400">{analysis.riskLevel}</span>
                  </p>
                  {/* <p className="mb-4">Confidence: {analysis.confidence}</p> */}
                  <div>
                    <h4 className="font-semibold mb-2">Transcript:</h4>
                    <p className="text-primary-200">{analysis.transcript}</p>
                  </div>
                  <div>
                    <h4 className="font-semibold mb-2">Analysis & Feedba:</h4>
                    <p className="text-primary-200">{analysis.transcript}</p>
                  </div>
                </div>
              </motion.div>
            )}
          </motion.div>
        </div>
      </section>

      {/* Footer */}
      <footer className="py-12 bg-primary-900">
        <div className="container mx-auto px-6 text-center">
          <p className="text-primary-100/60">© 2025 ScamShield. All rights reserved.</p>
        </div>
      </footer>
    </div>
  );
}

export default App;
