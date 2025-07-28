import { useState } from 'react'
import { uploadFile } from '../services/api'
import React from 'react';


function UploadForm() {
  const [file, setFile] = useState(null)
  const [prompt, setPrompt] = useState('')
  const [response, setResponse] = useState('')

  const handleSubmit = async (e) => {
    e.preventDefault()
    if (!file || !prompt) {
      alert("Please provide both a file and prompt!")
      return
    }

    try {
      const res = await uploadFile(file, "user@example.com", prompt)  // Replace with dynamic email if needed
      setResponse(res.answer || 'No response from server.')
    } catch (err) {
      console.error(err)
      setResponse('Error: Could not process your request.')
    }
  }

  return (
    <div>
      <h2>Upload File & Ask a Question</h2>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={(e) => setFile(e.target.files[0])} />
        <br />
        <textarea
          placeholder="Enter your prompt here..."
          value={prompt}
          onChange={(e) => setPrompt(e.target.value)}
          rows={4}
          cols={50}
        />
        <br />
        <button type="submit">Submit</button>
      </form>
      {response && (
        <div style={{ marginTop: '20px', whiteSpace: 'pre-wrap' }}>
          <strong>Response:</strong>
          <p>{response}</p>
        </div>
      )}
    </div>
  )
}

export default UploadForm
