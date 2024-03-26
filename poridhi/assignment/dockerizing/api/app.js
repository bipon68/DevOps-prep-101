const express = require('express')
const cors = require('cors')

const app = express()

app.use(cors())

app.get('/', (req, res) => {
  res.json([
    {
      "id":"1",
      "title":"Book Review: Software Engineering Alap"
    },
    {
      "id":"2",
      "title":"Book Review: Fullstack Development connection the Dots"
    },
    {
      "id":"3",
      "title":"Book Review: Atomic Habits"
    }
  ])
})

app.listen(4000, () => {
  console.log('listening for requests on port 4000')
})