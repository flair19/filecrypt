# FileCrypt

A comprehensive file encryption and decryption application that provides secure handling of various file types including text, images, audio, and video files.

## Features

- Text encryption/decryption with symmetric key encryption
- File encryption support for multiple formats:
  - Documents (.txt, .pdf, .doc, etc.)
  - Images (.jpg, .png, .gif, etc.)
  - Audio (.mp3, .wav, .flac, etc.)
  - Video (.mp4, .avi, .mov, etc.)
- Secure key management
- Error detection and corruption verification
- Clean and intuitive web interface
- REST API endpoints for programmatic access

## Tech Stack

### Backend
- Python 3.8+
- FastAPI (API framework)
- Cryptography.io (encryption library)
- Uvicorn (ASGI server)

### Frontend
- React
- Tailwind CSS
- Lucide Icons

## Prerequisites

- Python 3.8 or higher
- Node.js 14.0 or higher
- pip (Python package manager)
- npm (Node.js package manager)
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/filecrypt.git
cd filecrypt
```

2. Set up Python virtual environment:
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate
```

3. Install backend dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the backend server:
```bash
# Make sure your virtual environment is activated
# From the project root directory:
uvicorn main:app --reload
```

2. Start the frontend development server:
```bash
# From the frontend directory:
npm start
```

3. Access the application:
- Web Interface: http://localhost:3000
- API Documentation: http://localhost:8000/docs
- Alternative API Documentation: http://localhost:8000/redoc

## API Endpoints

### Text Operations
- POST `/encrypt/text` - Encrypt text content
- POST `/decrypt/text` - Decrypt text content

### File Operations
- POST `/encrypt/file` - Encrypt any file
- POST `/decrypt/file` - Decrypt any file

### Audio Operations
- POST `/encrypt/audio` - Encrypt audio files
- POST `/decrypt/audio` - Decrypt audio files

### Video Operations
- POST `/encrypt/video` - Encrypt video files
- POST `/decrypt/video` - Decrypt video files

## Development Setup

### Required Tools
- VS Code, PyCharm, or Vim
- Git for version control
- Postman or similar for API testing

### VS Code Extensions
- Python
- Pylance
- React Extension Pack
- Tailwind CSS IntelliSense

## Security Considerations

1. Key Management:
   - Keys are generated using cryptographically secure methods
   - Keys are never stored in plaintext
   - Each session uses a unique encryption key

2. File Handling:
   - Secure temporary file management
   - Automatic cleanup of temporary files
   - Corruption detection during decryption

3. Error Handling:
   - Validation of file formats
   - Verification of encryption integrity
   - Proper error messages without leaking sensitive information

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## Testing

Run backend tests:
```bash
# From project root
pytest tests/
```

Run frontend tests:
```bash
# From frontend directory
npm test
```

## Project Structure
```
filecrypt/
├── backend/
│   ├── main.py
│   ├── decrypter.py
│   └── tests/
├── frontend/
│   ├── src/
│   ├── public/
│   └── package.json
├── requirements.txt
├── .env
└── README.md
```

## Requirements

```txt
fastapi==0.100.0
python-multipart==0.0.6
cryptography==41.0.1
uvicorn==0.22.0
python-dotenv==1.0.0
pytest==7.4.0
```

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Troubleshooting

Common issues and solutions:

1. Key Error:
   ```
   Solution: Regenerate encryption key using the provided utility
   ```

2. File Permission Issues:
   ```
   Solution: Check file permissions and user access rights
   ```

3. Dependency Conflicts:
   ```
   Solution: Clear pip cache and reinstall dependencies
   ```

For more issues, please check the GitHub Issues page.