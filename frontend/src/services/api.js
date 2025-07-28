// src/services/api.js

import axios from 'axios';

const API_BASE = 'http://localhost:8000'; // Update if backend URL changes

export const uploadFile = async (file, email, prompt) => {
  const formData = new FormData();
  formData.append('file', file);
  formData.append('email', email);
  formData.append('prompt', prompt);

  const response = await axios.post(`${API_BASE}/upload`, formData);
  return response.data;
};

export const exportPDF = async (email) => {
  const formData = new FormData();
  formData.append('email', email);

  const response = await axios.post(`${API_BASE}/export`, formData);
  return response.data;
};
