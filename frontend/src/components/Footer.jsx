export default function Footer() {
  return (
    <footer style={{
      background: "var(--brand-charcoal)",
      color: "var(--brand-cream2)",
      fontFamily: "Montserrat, sans-serif",
      fontSize: "13px"
    }}>
      {/* Main footer content */}
      <div style={{
        padding: "40px",
        display: "flex",
        justifyContent: "space-between",
        alignItems: "flex-start",
        maxWidth: "1200px",
        margin: "0 auto"
      }}>
        {/* Left column */}
        <div style={{ flex: 1 }}>
          <h3 style={{
            color: "white",
            fontWeight: "bold",
            fontSize: "16px",
            marginBottom: "8px"
          }}>
            AI Resume Builder
          </h3>
          <p style={{
            color: "var(--brand-cream2)",
            fontSize: "13px",
            lineHeight: "1.5",
            margin: 0
          }}>
            AI-powered resume building and career tools.
          </p>
        </div>

        {/* Center column */}
        <div style={{ flex: 1, display: 'flex', flexDirection: 'column', alignItems: 'center' }}>
          <div style={{ textAlign: 'left' }}>
            <h4 style={{
              color: "white",
              fontWeight: "600",
              fontSize: "14px",
              marginBottom: "16px"
            }}>
              Quick Links
            </h4>
            <div style={{ display: "flex", flexDirection: "column", gap: "8px" }}>
              <a href="/" style={{
                color: "var(--brand-cream2)",
                textDecoration: "none",
                fontSize: "13px"
              }}>
                Home
              </a>
              <a href="/dashboard" style={{
                color: "var(--brand-cream2)",
                textDecoration: "none",
                fontSize: "13px"
              }}>
                Dashboard
              </a>
              <a href="/resume-builder" style={{
                color: "var(--brand-cream2)",
                textDecoration: "none",
                fontSize: "13px"
              }}>
                Resume Builder
              </a>
              <a href="/skill-gap" style={{
                color: "var(--brand-cream2)",
                textDecoration: "none",
                fontSize: "13px"
              }}>
                Skill Gap
              </a>
              <a href="/jd-matcher" style={{
                color: "var(--brand-cream2)",
                textDecoration: "none",
                fontSize: "13px"
              }}>
                JD Matcher
              </a>
            </div>
          </div>
        </div>

        {/* Right column */}
        <div style={{ flex: 1, textAlign: 'right' }}>
          <h4 style={{
            color: "white",
            fontWeight: "600",
            fontSize: "14px",
            marginBottom: "16px"
          }}>
            Built for Students and Professionals
          </h4>
          <a
            href="https://github.com"
            target="_blank"
            rel="noopener noreferrer"
            style={{
              color: "var(--brand-cream2)",
              textDecoration: "none",
              fontSize: "13px"
            }}
          >
            View on GitHub
          </a>
        </div>
      </div>

      {/* Bottom bar */}
      <div style={{
        borderTop: "1px solid rgba(255, 255, 255, 0.08)",
        padding: "24px 40px",
        maxWidth: "1200px",
        margin: "0 auto",
        textAlign: "center"
      }}>
        <div style={{ fontSize: "12px", color: "var(--brand-cream2)" }}>
          © 2026 AI Resume Builder. All rights reserved. Built with care for smarter career growth.
        </div>
      </div>
    </footer>
  )
}