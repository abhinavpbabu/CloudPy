Hey, this is the old version.
the updated version is named "runwith.cloud" and can be accessed at https://github.com/thesophile/runwith.cloud.git
and the website will be available at [runwith.cloud](runwith.cloud)

# CloudPy

 Run Python libraries online with ease

 <img src="https://github.com/user-attachments/assets/6c703603-9cfc-483b-9f83-efb3fe6d9253" alt="screenshot" width="800" />

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

   **Install Docker**

  - [Debian](https://docs.docker.com/engine/install/debian/)
    
  - [Other systems](https://docs.docker.com/engine/install/)
    
5. **Run Migrations:**

    ```
    python manage.py migrate
    ```
    
6. **Start the Development Server:**

    ```
    python manage.py runserver
    ```



