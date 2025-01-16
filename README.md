# OSINT-red
osint framework to obtain information available on open source

## Process

```bash
git clone https://github.com/yajoDU10/OSINT-red.git
cd OSINT-red
```

1. Activate Python virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install packages:
   ```bash
   pip install instaloader h8mail holehe pyfiglet
   ```

3. Install tools using pipx:
   ```bash
   pipx install ghunt
   pipx install sherlock-project
   ```

4. Unzip required tools:
  ```bash
unzip camphish.zip -d camphish
unzip hound.zip -d hound
unzip phishmailer.zip -d phishmailer
unzip zphisher.zip -d zphisher
rm -rf camphish.zip hound.zip phishmailer.zip zphisher.zip
  ```

5. Set up PhishMailer:
   ```bash
   cd phishmailer
   chmod +x PhishMailer.py
   ```

6. Configure GHunt:
   - Run the command:
     ```bash
     ghunt login
     ```
   - Add the GHunt extension to your browser.
   - Get the OAuth code from the browser and paste it into the terminal after selecting the OAuth option.

7. Deactivate the virtual environment:
   ```bash
   deactivate
   ```

## Usage

To use the OSINT-red tool,
1. activate virtual environment
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```
2. run main.py file
   ```bash
   python3 main.py
   ```
3. deactivate virtual environment
   ```bash
   deactivate
   ```
