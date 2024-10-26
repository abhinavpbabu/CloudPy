# CloudPy

 Run Python libraries online with ease

 <img src="https://github.com/user-attachments/assets/1a9ee16a-3812-4ab7-82ea-43bb53d383de" alt="screenshot" width="800" />

## Key Features
  
 - No need to install libraries or manage dependencies.
 - Continue your work seamlessly across different devices.
 - Run in mobile phones and tablets with ease.
   
 Visit [cloudpy.online](https://cloudpy.online) to use the website.
 


## Local Installation

### Prerequisites

- **Python:** 3.11 (tested), but other versions may work.
- **Virtualenv** (optional but recommended)
- **Git**
- **pip**: For installing Python packages.

 

### Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/thesophile/CloudPy.git 
   cd CloudPy
   ```
2. **Create a Virtual Environment:**

    ```
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install Dependencies:**

    ```
    pip install -r requirements.txt
    ```

4.  **Install Docker**

  - [Debian](https://docs.docker.com/engine/install/debian/)
    
  - [Other systems](https://docs.docker.com/engine/install/)

5. **Set Permissions**
   
   Set appropriate permissions that the system can write to the media directory
   (Someone please tell me a better way to do this)
   
   ```
   sudo chown -R your_username:your_username /path/to/your/project/media
   ```
   
   > [!IMPORTANT]  
   > Without doing this, The site won't work properly.
    
6. **Run Migrations:**

    ```
    python manage.py migrate
    ```
    
7. **Start the Development Server:**

    ```
    python manage.py runserver
    ```


