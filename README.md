<div align="center">
<h1 align="center">
<img src="https://cf-assets.www.cloudflare.com/slt3lc6tev37/CHOl0sUhrumCxOXfRotGt/081f81d52274080b2d026fdf163e3009/cloudflare-icon-color_3x.png" width="100" />
<br>Cloudflare
</h1>
<h2>Infrastructure-as-Code via Pulumi</h2>
<h3>Developed with the following:</h3>

<p align="center">
<img src="https://img.shields.io/badge/Pulumi-8A3391.svg?style&logo=Pulumi&logoColor=white" alt="Pulumi" />
<img src="https://img.shields.io/badge/Python-3776AB.svg?style&logo=Python&logoColor=white" alt="Python" />
<img src="https://img.shields.io/badge/GitHub%20Actions-2088FF.svg?style&logo=GitHub-Actions&logoColor=white" alt="GitHub%20Actions" />
</p>
<img src="https://img.shields.io/github/languages/top/etcollective/cloudflare?style&color=5D6D7E" alt="GitHub top language" />
<img src="https://img.shields.io/github/languages/code-size/etcollective/cloudflare?style&color=5D6D7E" alt="GitHub code size in bytes" />
<img src="https://img.shields.io/github/commit-activity/m/etcollective/cloudflare?style&color=5D6D7E" alt="GitHub commit activity" />
<img src="https://img.shields.io/github/license/etcollective/cloudflare?style&color=5D6D7E" alt="GitHub license" />
</div>

---

## 📒 Table of Contents
- [📒 Table of Contents](#-table-of-contents)
- [📍 Overview](#-overview)
- [⚙️ Features](#-features)
- [📂 Project Structure](#project-structure)
- [🧩 Modules](#modules)
- [🚀 Getting Started](#-getting-started)
- [🗺 Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📄 License](#-license)
- [👏 Acknowledgments](#-acknowledgments)

---


## 📍 Overview

The project defines global configuration for ETC's Cloudflare environment. CI/CD is provider via GitHub Actions.

---
## 🧩 Modules

<details closed><summary>Root</summary>

| File                                                                            | Summary                                                                                                                                                                                                                                                                                                                                                      |
| ---                                                                             | ---                                                                                                                                                                                                                                                                                                                                                          |
| [__main__.py](https://github.com/etcollective/cloudflare/blob/main/__main__.py) | This code imports Python modules from subdirectories and executes all callable functions in each module. It assumes that each subdirectory contains Python modules (files with a '.py' extension) and skips the'__init__.py' file. The code iterates through the directories, imports the modules, and executes all callable functions found in each module. |

</details>

<details closed><summary>Account</summary>

| File                                                                                  | Summary                                                                                                                                                                                                                                                                                                  |
| ---                                                                                   | ---                                                                                                                                                                                                                                                                                                      |
| [members.py](https://github.com/etcollective/cloudflare/blob/main/account/members.py) | This code adds admin members with superadmin privileges to a Cloudflare account using the pulumi_cloudflare library. These admins are specified by their email addresses and assigned a specific role ID. The code ensures that each admin is associated with the account using parent resource options. |
| [account.py](https://github.com/etcollective/cloudflare/blob/main/account/account.py) | This code sets up a Cloudflare account with specified configurations and exports the account ID for further use.                                                                                                                                                                                         |

</details>

<details closed><summary>Dns_records</summary>

| File                                                                                                              | Summary                                                                                                                                                                                                                                                                                        |
| ---                                                                                                               | ---                                                                                                                                                                                                                                                                                            |
| [mx_records.py](https://github.com/etcollective/cloudflare/blob/main/dns_records/mx_records.py)                   | This code creates MX records in Cloudflare for Google Workspace email using pulumi and the pulumi_cloudflare library.                                                                                                                                                                          |
| [gsuite_verification.py](https://github.com/etcollective/cloudflare/blob/main/dns_records/gsuite_verification.py) | This code sets up DNS records for verifying Google Workspace and support accounts via Cloudflare DNS. It creates CNAME records with TTL of 3600 seconds.                                                                                                                                       |
| [website.py](https://github.com/etcollective/cloudflare/blob/main/dns_records/website.py)                         | This code sets up DNS records for a staging website and a production website using the pulumi_cloudflare library. The staging website uses a CNAME record, while the production website uses A and AAAA records for both root and www subdomains. The records are proxied and have a TTL of 1. |
| [atlassian.py](https://github.com/etcollective/cloudflare/blob/main/dns_records/atlassian.py)                     | This code creates DNS records in Cloudflare for domain verification and email authentication for an Atlassian service.                                                                                                                                                                         |

</details>

<details closed><summary>Domain</summary>

| File                                                                           | Summary                                                                                                                                                                                                        |
| ---                                                                            | ---                                                                                                                                                                                                            |
| [zone.py](https://github.com/etcollective/cloudflare/blob/main/domain/zone.py) | This code sets up a Cloudflare zone for the specified domain with the specified account ID and plan.The zone is set to be not paused and to have a type of "full".The zone ID is then exported for future use. |

</details>

---

## 🚀 Getting Started

### ✔️ Prerequisites

Before you begin, ensure that you have the following prerequisites installed:
> - `ℹ️ pulumi`
> - `ℹ️ Python`
> - `ℹ️ Dependencies defined in requirements.txt`

### 📦 Installation

1. Clone the cloudflare repository:
```sh
git clone https://github.com/etcollective/cloudflare
```

2. Change to the project directory:
```sh
cd cloudflare
```

3. Install the dependencies:
```sh
pip install -r requirements.txt
```

### 🎮 Using Pulumi

```sh
pulumi up
```
---