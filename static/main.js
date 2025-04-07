document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("startForm");
    const statusDiv = document.getElementById("status");
    let matchId = null;
  
    form.addEventListener("submit", async (e) => {
      e.preventDefault();
      const player1 = document.getElementById("player1").value.trim();
      const player2 = document.getElementById("player2").value.trim();
      const rating = parseInt(document.getElementById("rating").value) || 1200;
      const duration = parseInt(document.getElementById("duration").value) || 600;
  
      const res = await fetch('/start_match', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ player1, player2, rating, duration })
      });
  
      const data = await res.json();
      if (res.ok) {
        matchId = data.match_id;
        const link = data.problem.url;
        statusDiv.innerHTML = `
          <p>Match started!</p>
          <p><a href="${link}" target="_blank">Solve this problem</a></p>
          <p>Waiting for submissions...</p>
        `;
        pollMatchStatus();
      } else {
        statusDiv.innerHTML = `<p style="color:red;">Error: ${data.error}</p>`;
      }
    });
  
    async function pollMatchStatus() {
      const interval = setInterval(async () => {
        if (!matchId) return;
        const res = await fetch(`/check_match?match_id=${matchId}`);
        const data = await res.json();
  
        if (data.winner) {
          clearInterval(interval);
          statusDiv.innerHTML += `<p><strong>Winner: ${data.winner}</strong></p>`;
        }
      }, 5000);
    }
  });
  