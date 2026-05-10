import { useState } from 'react'
import Navbar from '../components/Navbar'

export default function JDMatcher() {
  const [jobDescription, setJobDescription] = useState("")
  const [resumeFile, setResumeFile] = useState(null)
  const [result, setResult] = useState(null)
  const [loading, setLoading] = useState(false)
  const [error, setError] = useState(null)

  const handleFileChange = (e) => {
    setError(null)
    const file = e.target.files[0]
    if (file) {
      if (!file.name.toLowerCase().endsWith('.pdf') && !file.name.toLowerCase().endsWith('.docx')) {
        setError('Only PDF or DOCX resume files are allowed')
        setResumeFile(null)
        return
      }
      setResumeFile(file)
    }
  }

  const handleAnalyze = async () => {
    if (!jobDescription.trim() || !resumeFile) {
      setError('Please provide both a job description and a resume file.')
      return
    }
    setLoading(true)
    setError(null)
    setResult(null)
    try {
      const formData = new FormData()
      formData.append('job_description', jobDescription)
      formData.append('resume', resumeFile)

      const response = await fetch(`${import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'}/api/jd-match`, {
        method: 'POST',
        body: formData
      })

      if (!response.ok) {
        const errorText = await response.text()
        throw new Error(errorText || `Request failed with status ${response.status}`)
      }

      const data = await response.json()
      setResult(data)
    } catch (err) {
      setError(err?.message || 'Something went wrong. Make sure the backend is running.')
    } finally {
      setLoading(false)
    }
  }

  return (
    <div>
      <Navbar page="app" />

      {/* Header Bar */}
      <header style={{
        background: "var(--brand-charcoal)",
        padding: "52px 40px",
        paddingTop: "72px",
        textAlign: "center"
      }} className="skill-gap-header">
        <h1 style={{
          fontSize: "34px",
          fontWeight: "800",
          color: "var(--brand-cream)",
          marginBottom: "8px"
        }} className="skill-gap-heading">
          JD Keyword Matcher
        </h1>
        <p style={{
          fontSize: "16px",
          color: "var(--brand-olive-lt)"
        }}>
          Upload your resume to analyze its content
        </p>
      </header>

      {/* Content */}
      <main style={{
        background: "var(--section-bg)",
        padding: "48px 24px"
      }}>
        <div style={{
          maxWidth: "1000px",
          margin: "0 auto"
        }}>
          {/* Input Section */}
          <div style={{
            background: "white",
            borderRadius: "16px",
            border: "1px solid #ebebeb",
            boxShadow: "0 2px 12px rgba(0,0,0,0.04)",
            padding: "28px 32px",
            marginBottom: "24px"
          }}>
            <form onSubmit={(e) => e.preventDefault()} style={{ margin: 0 }}>
            <div style={{
              display: "grid",
              gridTemplateColumns: "1fr",
              gap: "24px",
              marginBottom: "32px"
            }}>
              <div>
                <label style={{
                  fontSize: "12px",
                  fontWeight: "700",
                  textTransform: "uppercase",
                  letterSpacing: "0.06em",
                  color: "var(--brand-charcoal)",
                  display: "block",
                  marginBottom: "8px"
                }}>
                  Job Description
                </label>
                <textarea
                  value={jobDescription}
                  onChange={(e) => setJobDescription(e.target.value)}
                  placeholder="Paste the job description here..."
                  style={{
                    width: "100%",
                    minHeight: "180px",
                    border: "1px solid #ebebeb",
                    borderRadius: "12px",
                    fontFamily: "Montserrat",
                    padding: "16px",
                    fontSize: "14px",
                    resize: "vertical",
                    outline: "none",
                    background: "white",
                    color: "var(--brand-charcoal)"
                  }}
                />
              </div>

              <div>
                <label style={{
                  fontSize: "12px",
                  fontWeight: "700",
                  textTransform: "uppercase",
                  letterSpacing: "0.06em",
                  color: "var(--brand-charcoal)",
                  display: "block",
                  marginBottom: "8px"
                }}>
                  Resume
                </label>
                <div style={{
                  border: "1px dashed #d8d8d8",
                  borderRadius: "12px",
                  padding: "20px",
                  background: "#fafafa"
                }}>
                  <input
                    type="file"
                    accept=".pdf,.docx,application/pdf,application/vnd.openxmlformats-officedocument.wordprocessingml.document"
                    onChange={handleFileChange}
                    style={{ width: "100%" }}
                  />
                  {resumeFile && (
                    <div style={{
                      marginTop: "14px",
                      color: "var(--brand-charcoal)",
                      fontSize: "14px"
                    }}>
                      Selected file: {resumeFile.name}
                    </div>
                  )}
                </div>
              </div>
            </div>

            {/* Analyze Button */}
            <div style={{ textAlign: "center" }}>
              <button
                type="button"
                onClick={handleAnalyze}
                disabled={loading || !resumeFile}
                style={{
                  background: "var(--brand-olive)",
                  color: "white",
                  borderRadius: "40px",
                  padding: "14px 36px",
                  fontSize: "16px",
                  fontWeight: "700",
                  cursor: loading || !resumeFile ? "not-allowed" : "pointer",
                  border: "none",
                  opacity: loading || !resumeFile ? 0.6 : 1
                }}
              >
                {loading ? "Analyzing..." : "Analyze Match"}
              </button>
            </div>
            </form>
          </div>

          {/* Error Message */}
          {error && (
            <div style={{
              background: "rgba(193,18,31,0.08)",
              borderLeft: "4px solid #c1121f",
              color: "#c1121f",
              borderRadius: "8px",
              padding: "14px 18px",
              fontSize: "14px",
              marginBottom: "24px"
            }}>
              {error}
            </div>
          )}

          {/* Results Section */}
          {result && (
            <div>
              {/* Match Score */}
              <div style={{
                background: "white",
                borderRadius: "16px",
                border: "1px solid #ebebeb",
                boxShadow: "0 2px 12px rgba(0,0,0,0.04)",
                padding: "32px",
                textAlign: "center",
                marginBottom: "24px"
              }}>
                <div style={{
                  fontSize: "48px",
                  fontWeight: "800",
                  color: "var(--brand-olive)",
                  marginBottom: "8px"
                }}>
                  {result.score}%
                </div>
                <div style={{
                  fontSize: "16px",
                  fontWeight: "600",
                  color: "var(--brand-charcoal)"
                }}>
                  Keyword Match Score
                </div>
              </div>

              {/* Keywords */}
              <div style={{
                display: "grid",
                gridTemplateColumns: "repeat(auto-fit, minmax(400px, 1fr))",
                gap: "24px",
                marginBottom: "24px"
              }}>
                {/* Matched Keywords */}
                <div style={{
                  background: "white",
                  borderRadius: "16px",
                  border: "1px solid #ebebeb",
                  boxShadow: "0 2px 12px rgba(0,0,0,0.04)",
                  padding: "28px"
                }}>
                  <h3 style={{
                    fontSize: "16px",
                    fontWeight: "700",
                    marginBottom: "16px",
                    color: "var(--brand-charcoal)"
                  }}>
                    Matched Keywords
                  </h3>
                  <div style={{
                    display: "flex",
                    flexWrap: "wrap",
                    gap: "8px"
                  }}>
                    {result.matched.map((keyword, index) => (
                      <span key={index} style={{
                        background: "var(--brand-olive-lt)",
                        color: "var(--brand-olive-dk)",
                        padding: "6px 12px",
                        borderRadius: "20px",
                        fontSize: "13px",
                        fontWeight: "600"
                      }}>
                        {keyword}
                      </span>
                    ))}
                  </div>
                </div>

                {/* Missing Keywords */}
                <div style={{
                  background: "white",
                  borderRadius: "16px",
                  border: "1px solid #ebebeb",
                  boxShadow: "0 2px 12px rgba(0,0,0,0.04)",
                  padding: "28px"
                }}>
                  <h3 style={{
                    fontSize: "16px",
                    fontWeight: "700",
                    marginBottom: "16px",
                    color: "var(--brand-charcoal)"
                  }}>
                    Missing Keywords
                  </h3>
                  <div style={{
                    display: "flex",
                    flexWrap: "wrap",
                    gap: "8px"
                  }}>
                    {result.missing.map((keyword, index) => (
                      <span key={index} style={{
                        background: "#ebebeb",
                        color: "var(--brand-charcoal)",
                        padding: "6px 12px",
                        borderRadius: "20px",
                        fontSize: "13px",
                        fontWeight: "600"
                      }}>
                        {keyword}
                      </span>
                    ))}
                  </div>
                </div>
              </div>

              {/* Suggestion */}
              <div style={{
                background: "var(--section-bg)",
                borderRadius: "12px",
                padding: "20px",
                border: "1px solid #ebebeb"
              }}>
                <p style={{
                  fontSize: "15px",
                  lineHeight: "1.6",
                  color: "var(--brand-charcoal)",
                  margin: 0
                }}>
                  {result.suggestion}
                </p>
              </div>
            </div>
          )}
        </div>
      </main>
    </div>
  )
}