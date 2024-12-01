
# Automation Scripts

This repository contains simple yet powerful automation scripts designed to make your life easier. Each script requires minimal setup and takes a directory as a parameter to perform its function.  

Additionally, you can easily add all scripts in this repository to your system's PATH for seamless access.

---

## Table of Contents

- [Scripts Overview](#scripts-overview)
  - [group_files.py](#group_filespy)
  - [addto_path.py](#addto_pathpy)
- [Setup and Usage](#setup-and-usage)
  - [Running Individual Scripts](#running-individual-scripts)
  - [Adding Scripts to PATH](#adding-scripts-to-path)
- [Contributing](#contributing)
- [License](#license)

---

## Scripts Overview

### `group_files.py`
Organize files within a specified directory by grouping them based on criteria like file type, size, or any custom logic implemented in the script.

- **Usage:**  
  ```bash
  python group_files.py <directory>
  ```
- **Example:**  
  ```bash
  python group_files.py /path/to/your/folder
  ```

### `addto_path.py`
Add a specified directory to your system's PATH, allowing you to execute scripts and binaries from that directory without providing the full path.

- **Usage:**  
  ```bash
  python addto_path.py <directory>
  ```
- **Example:**  
  ```bash
  python addto_path.py /path/to/your/folder
  ```

---

## Setup and Usage

### Running Individual Scripts

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/automation-scripts.git
   cd automation-scripts
   ```

2. Run the desired script:
   - For `group_files.py`:
     ```bash
     python group_files.py <directory>
     ```
   - For `addto_path.py`:
     ```bash
     python addto_path.py <directory>
     ```

---

### Adding Scripts to PATH

To make all scripts in this repository accessible globally:

1. Navigate to the repository directory:
   ```bash
   cd /path/to/automation-scripts
   ```

2. Add the repository directory to your PATH using `addto_path.py`:
   ```bash
   python addto_path.py /path/to/automation-scripts
   ```

3. After adding to PATH, you can directly run scripts from anywhere:
   - Example:  
     ```bash
     group_files.py /path/to/directory
     ```

---

## Contributing

Contributions are welcome! If you have ideas for new scripts or improvements to existing ones, feel free to submit a pull request. Follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a brief description of your feature"
   ```
4. Push the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Let me know if you'd like further customization or additional details!
