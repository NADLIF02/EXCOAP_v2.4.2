const express = require('express');
const bodyParser = require('body-parser');
const app = express();

app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

app.post('/submit-leave-request', (req, res) => {
    console.log('Received leave request:', req.body);
    res.status(200).send('Leave request received');
});

const PORT = 5000;
app.listen(PORT, () => {
    console.log(`Server running on http://192.168.1.68:${PORT}`);
});
