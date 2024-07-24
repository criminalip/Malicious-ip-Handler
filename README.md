# Malicious-ip-Handler
 
This project involves collecting malicious IP addresses detected by the Criminal IP service, adding new IP addresses to a file, and automatically deleting old IP addresses.

## Introduction
In the ever-evolving landscape of cybersecurity, staying ahead of potential threats is crucial. Criminal IP offers a real-time threat hunting search engine that specializes in OSINT-based Cyber Threat Intelligence (CTI). By leveraging the Criminal IP service, this project aims to provide an efficient and automated way to manage malicious IP addresses, helping organizations enhance their security measures.

For more information or to request access to our complete dataset, please visit our [Contact Us](https://www.criminalip.io/contact-us) page.

## Key Features
 
- **Fetch Malicious IP List**: Retrieve the latest list of malicious IP addresses classified by the Criminal IP service.
- **Add New IP**: Add newly detected malicious IP addresses from Criminal IP to a CSV or JSON file.
- **Delete Old IPs**: Automatically delete IP addresses older than 7 days and generate a CSV or JSON file of the deleted IPs.
 
## Prerequisites
 
- **Criminal IP API KEY**: Log in to [Criminal IP](https://www.criminalip.io/mypage/information), copy your API_KEY, and use it.
 
## Installation
 
Download the project files:
```bash
git clone https://github.com/criminalip/Malicious-ip-Handler.git
```
 
fire_config.py setting:
Set the CRIMINALIP_API_KEY value
 
## Project Structure
```bash
📦malicious_ip_management_project
┣ 📂core
┃ ┗ 📂api
┃ ┃ ┣ 📂input
┃ ┃ ┣ 📂output
┃ ┃ ┣ 📜cip_request_get_ip.py
┃ ┃ ┗ 📜managefiles.py
┣ 📂log
┣ 📜cip_c2_detect_query.json
┣ 📜config.py
┗ 📜main.py 
```
 
## Usage
 
```bash
python main.py
```
 
## Example
Example file format for newly added IPs / IPs to be deleted

#### CSV
![CSV FILE](https://github.com/user-attachments/assets/5e7cc2c8-e34e-4084-9e18-053ff5cda1db)

#### JSON
![JSON FILE](https://github.com/user-attachments/assets/7ee6e651-6369-4404-92bf-6d376bcd5061)
