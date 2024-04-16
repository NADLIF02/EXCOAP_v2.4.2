const express = require('express');
const bodyParser = require('body-parser');

const app = express();
const PORT = 3000;

// Middleware to parse JSON and urlencoded form data
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

// Route to handle POST request
app.post('/submit-leave-request', (req, res) => {
    console.log(req.body); // Log the submitted data to the console
    res.send('Leave request submitted successfully!'); // Send a response back to the client
});

app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
