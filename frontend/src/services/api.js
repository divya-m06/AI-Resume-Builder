import axios from "axios"
const api = axios.create({
  baseURL: import.meta.env.VITE_API_BASE_URL || "http://localhost:8000",
  headers: { "Content-Type": "application/json" },
})

export const analyzeJD = (jdText, resumeText) =>
  api.post("/api/jd-match", { jd_text: jdText, resume_text: resumeText })

export default api