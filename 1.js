const { exec } = require("child_process");

// Initialize a counter for the commit message
let commitCount = 1;

setInterval(() => {
  // Use the current commit count in the commit message
  exec(`git add . && git commit -m "shawon commit ${commitCount}" && git push origin main`, (error, stdout, stderr) => {
    if (error) {
      console.error(`Error: ${error}`);
      return;
    }
    console.log(`Output: ${stdout}`);
    console.log(`Auto commit ${commitCount} pushed successfully.`);
    
    // Increment the commit counter
    commitCount++;
  });
}, 50000);
