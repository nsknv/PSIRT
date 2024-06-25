

 NVIDIA DGX Station A100 and DGX Station A800 - February 2024
===============================================================================




 Updated 02/08/2024 07:34 PM



NVIDIA has released a firmware security update for the NVIDIA DGX™ Station A100 and DGX™ Station A800 systems.


To protect your system, download and install this firmware update through the [NVIDIA Enterprise Support Portal](https://nvid.nvidia.com/dashboard/).


Go to [NVIDIA Product Security](https://www.nvidia.com/security/).






---




### Details


This section provides a summary of potential vulnerabilities that this security update addresses and their impact. Descriptions use [CWE™](https://cwe.mitre.org/), and base scores and vectors use [CVSS v3.1](https://www.first.org/cvss/specification-document) standards.


| CVE ID | Description | Vector | Base Score | Severity | CWE | Impacts |
|:---------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:------------------------------------|-------------:|:-----------|:--------|:----------------------------------------------------------------------------------------------------|
| CVE‑2022‑42271 | NVIDIA DGX Station A100 and DGX Station A800 baseboard management controller (BMC) contains a vulnerability in the Intelligent Platform Management Interface (IPMI) handler, where an attacker with the required privileges can cause a buffer overflow, which may lead to denial of service or code execution. | AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H | 8.4 | High | CWE-120 | Denial of service, code execution |
| CVE‑2022‑42272 | NVIDIA DGX Station A100 and DGX Station A800 BMC contains a vulnerability in the IPMI handler, where an attacker with the required privileges can cause a buffer overflow, which may lead to code execution, denial of service, or escalation of privileges. | AV:N/AC:H/PR:N/UI:N/S:U/C:H/I:H/A:H | 8.1 | High | CWE-120 | Denial of service, code execution, escalation of privileges |
| CVE‑2022‑42273 | NVIDIA DGX Station A100 and DGX Station A800 BMC contains a vulnerability in libwebsocket, where an attacker with the required privileges can cause a buffer overflow, which may lead to denial of service or code execution. | AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N | 8.1 | High | CWE-120 | Denial of service, code execution |
| CVE‑2022‑42274 | NVIDIA DGX Station A100 and DGX Station A800 BMC contains a vulnerability in the IPMI handler, where an attacker with the required privileges can cause a buffer overflow, which may lead to denial of service or code execution. | AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H | 7.8 | High | CWE-120 | Denial of service, code execution |
| CVE‑2022‑42275 | NVIDIA DGX Station A100 and DGX Station A800 BMC contains a vulnerability in the IPMI handler, where an unauthenticated host is allowed to write to a host SPI flash, bypassing secure boot protections. An exploit of this vulnerability may lead to a loss of integrity or denial of service. | AV:L/AC:L/PR:N/UI:N/S:U/C:N/I:H/A:H | 7.7 | High | CWE-120 | Denial of service, integrity loss |
| CVE-2023-31032 | NVIDIA DGX Station A100 and DGX Station A800 SBIOS contains a vulnerability where a user may cause a dynamic variable evaluation by local access. A successful exploit of this vulnerability may lead to denial of service. | AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H | 7.5 | High | CWE-627 | Denial of service |
| CVE‑2023‑25521 | NVIDIA DGX Station A100 and DGX Station A800 SBIOS contains a vulnerability where improper validation of an input parameter may lead to code execution, escalation of privileges, denial of service, information disclosure, and data tampering. | AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H | 7.5 | High | CWE-250 | Code execution, escalation of privileges, denial of service, information disclosure, data tampering |
| CVE‑2022‑42279 | NVIDIA DGX Station A100 and DGX Station A800 BMC contains a vulnerability in the SPX REST API, where an attacker with the required privileges can inject arbitrary shell commands, which may lead to code execution, denial of service, information disclosure, or data tampering. | AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H | 7.2 | High | CWE-78 | Code execution, denial of service, information disclosure, data tampering |
| CVE‑2022‑42289 | NVIDIA DGX Station A100 and DGX Station A800 BMC contains a vulnerability in the SPX REST API, where an attacker with the required privileges can inject arbitrary shell commands, which may lead to code execution, denial of service, information disclosure, or data tampering. | AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H | 7.2 | High | CWE-78 | Code execution, denial of service, information disclosure, data tampering |
| CVE‑2022‑42290 | NVIDIA DGX Station A100 and DGX Station A800 BMC contains a vulnerability in the SPX REST API, where an attacker with the required privileges can inject arbitrary shell commands, which may lead to code execution, denial of service, information disclosure, or data tampering. | AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H | 7.2 | High | CWE-78 | Code execution, denial of service, information disclosure, data tampering |
| CVE‑2022‑42280 | NVIDIA DGX Station A100 and DGX Station A800 BMC contains a vulnerability in the SPX REST authorization handler, where an unauthorized attacker can exploit a path traversal, which may lead to escalation of privileges. | AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:N | 7.1 | High | CWE-22 | Escalation of privileges |
| CVE-2023-31034 | NVIDIA DGX Station A100 and DGX Station A800 SBIOS contains a vulnerability where a local attacker can cause input validation checks to be bypassed by causing an integer overflow. A successful exploit of this vulnerability may lead to denial of service, information disclosure, and data tampering. | AV:L/AC:H/PR:L/UI:R/S:C/C:L/I:L/A:H | 6.6 | Medium | CWE-190 | Denial of service, information disclosure, data tampering |
| CVE‑2022‑42282 | NVIDIA DGX Station A100 and DGX Station A800 BMC contains a vulnerability in the SPX REST API, where an attacker with the required privileges can access arbitrary files, which may lead to information disclosure. | AV:N/AC:L/PR:L/UI:N/S:U/C:H/I:N/A:N | 6.5 | Medium | CWE-22 | Information disclosure |
| CVE‑2022‑42283 | NVIDIA DGX Station A100 and DGX Station A800 BMC contains a vulnerability in the IPMI handler, where an attacker with the required privileges can cause a buffer overflow, which may lead to denial of service or code execution. | AV:L/AC:H/PR:H/UI:N/S:U/C:H/I:H/A:H | 6.4 | Medium | CWE-120 | Denial of service, code execution |
| CVE‑2022‑42284 | NVIDIA DGX Station A100 and DGX Station A800 BMC stores user passwords in an obfuscated form in a database accessible by the host, which may lead to exposure of user credentials. | AV:L/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N | 6.2 | Medium | CWE-312 | Credential exposure |
| CVE‑2022‑42287 | NVIDIA DGX Station A100 and DGX Station A800 BMC contains a vulnerability in the IPMI handler, where an attacker can upload and download arbitrary files under certain circumstances, which may lead to denial of service, escalation of privileges, information disclosure, or data tampering. | AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:N | 6 | Medium | CWE-22 | Denial of service, escalation of privileges, information disclosure, data tampering |
| CVE‑2022‑42288 | NVIDIA DGX Station A100 and DGX Station A800 BMC contains a vulnerability in the IPMI handler, where an unauthorized attacker can use certain oracles to guess a valid BMC username, which may lead to information disclosure. | AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:N/A:N | 5.3 | Medium | CWE-208 | Information disclosure |
| CVE-2023-31031 | NVIDIA DGX Station A100 and DGX Station A800 SBIOS contains a vulnerability where a user may cause a heap-based buffer overflow by local access. A successful exploit of this vulnerability may lead to code execution, denial of service, information disclosure, and data tampering. | AV:L/AC:L/PR:H/UI:N/S:U/C:L/I:L/A:L | 4.2 | Medium | CWE-122 | Code execution, denial of service, information disclosure, data tampering |
The NVIDIA risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk to your local installation. NVIDIA recommends evaluating the risk to your specific configuration.


### Security Updates


The following table lists the NVIDIA products affected, versions affected, and the updated version that includes this security update.


Note: To get the updated BMC and SBIOS versions listed in the table, upgrade to the NVIDIA DGX Station A100 and DGX Station A800 Firmware Update Container Version 24.1.1. Firmware updates are available through the [NVIDIA Enterprise Support Portal](https://nvid.nvidia.com/dashboard/).


| CVE IDs Addressed | Affected Products | Platform or OS | Affected Versions | Updated Version |
|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------|:----------------------------------|:-------------------------------------------|:---------------------|
| CVE‑2022‑42271 CVE‑2022‑42272 CVE‑2022‑42273 CVE‑2022‑42274 CVE‑2022‑42275 CVE‑2022‑42279 CVE‑2022‑42280 CVE‑2022‑42282 CVE‑2022‑42283 CVE‑2022‑42284 CVE‑2022‑42287 CVE‑2022‑42288 CVE‑2022‑42289 CVE‑2022‑42290 | NVIDIA DGX Servers | DGX Station A100 DGX Station A800 | All BMC firmware versions prior to 2.09.00 | BMC Firmware 2.09.00 |
| CVE‑2023‑25521 CVE‑2023‑31031 CVE‑2023‑31032 CVE‑2023‑31034 | NVIDIA DGX Servers | DGX Station A100 DGX Station A800 | All SBIOS firmware versions prior to 10.20 | SBIOS Firmware 10.20 |
### Get the Most Up to Date Product Security Information


Visit the [NVIDIA Product Security](https://www.nvidia.com/security) page to


* Subscribe to security bulletin notifications
* See the current list of NVIDIA security bulletins
* Report a potential security issue in any NVIDIA supported product
* Learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT)


### Revision History


| Revision | Date | Description |
|-----------:|:-----------------|:----------------|
| 1 | February 8, 2024 | Initial release |
### Support


If you have any questions about this security bulletin, contact [NVIDIA Support](https://www.nvidia.com/object/support.html).


##### Disclaimer


ALL NVIDIA INFORMATION, DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS (TOGETHER AND SEPARATELY, “MATERIALS”) ARE BEING PROVIDED “AS IS.” NVIDIA MAKES NO WARRANTIES, EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE MATERIALS, AND ALL EXPRESS OR IMPLIED CONDITIONS, REPRESENTATIONS AND WARRANTIES, INCLUDING ANY IMPLIED WARRANTY OR CONDITION OF TITLE, MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT, ARE HEREBY EXCLUDED TO THE MAXIMUM EXTENT PERMITTED BY LAW.


Information is believed to be accurate and reliable at the time it is furnished. However, NVIDIA Corporation assumes no responsibility for the consequences of use of such information or for any infringement of patents or other rights of third parties that may result from its use. No license is granted by implication or otherwise under any patent or patent rights of NVIDIA Corporation. Specifications mentioned in this publication are subject to change without notice. This publication supersedes and replaces all information previously supplied. NVIDIA Corporation products are not authorized for use as critical components in life support devices or systems without express written approval of NVIDIA Corporation.










Is this answer helpful?
-----------------------



Yes
No







Answers others found helpful
----------------------------


* [ NVIDIA GPU Display Driver - October 2023](/app/answers/detail/a_id/5491/related/1)
* [ NVIDIA GeForce NOW for Android - August 2023](/app/answers/detail/a_id/5476/related/1)
* [ NVIDIA DGX A100 and DGX A800 - June 2023](/app/answers/detail/a_id/5461/related/1)
* [ NVIDIA CUDA Toolkit - March 2023](/app/answers/detail/a_id/5446/related/1)
* [ NVIDIA Jetson AGX Xavier Series, Jetson Xavier NX, Jetson TX1, Jetson TX2 Series (including Jetson TX2 NX), and Jetson Nano (including Jetson Nano 2GB) - June 2023](/app/answers/detail/a_id/5466/related/1)








