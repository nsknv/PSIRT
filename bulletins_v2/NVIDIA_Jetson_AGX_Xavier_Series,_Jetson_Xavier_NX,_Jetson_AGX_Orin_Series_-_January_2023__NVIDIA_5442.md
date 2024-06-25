

 NVIDIA Jetson AGX Xavier Series, Jetson Xavier NX, Jetson AGX Orin Series - January 2023
===========================================================================================================




 Updated 01/25/2023 10:05 AM



NVIDIA has released a software update for NVIDIA® Jetson AGX Xavier™ series, Jetson Xavier™ NX, and Jetson AGX Orin series in the NVIDIA JetPack™ software development kit (SDK). The update addresses security issues that may lead to escalation of privileges, compromised data integrity and confidentiality, and denial of service. To protect your system, download and install the latest NVIDIA JetPack SDK from [NVIDIA DevZone](https://developer.nvidia.com/embedded/downloads).


Go to [NVIDIA Product Security](https://www.nvidia.com/security/).






---




### Details


This section provides a summary of potential vulnerabilities that this security update addresses and their impact. Descriptions use [CWE™](https://cwe.mitre.org/), and base scores and vectors use [CVSS v3.1](https://www.first.org/cvss/v3.1/user-guide) standards.


| CVE ID | Description | Base Score | Vector |
|:---------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------:|:------------------------------------|
| CVE‑2022‑42270 | NVIDIA distributions of Linux contain a vulnerability in nvdla\_emu\_task\_submit, where unvalidated input may allow a local attacker to cause stack-based buffer overflow in kernel code, which may lead to escalation of privileges, compromised data integrity and confidentiality, and denial of service. | 7.8 | AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H |
The NVIDIA risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk to your local installation. NVIDIA recommends consulting a security or IT professional to evaluate the risk to your specific configuration.


### Security Updates


The following table lists the NVIDIA software products affected, versions affected, and the updated version that includes this security update.


| CVE IDs Addressed | Software Product | Operating System | Affected Versions | Updated Version |
|:--------------------|:--------------------------------------------------------------------------|:-------------------|:--------------------------|:------------------|
| CVE‑2022‑42270 | NVIDIA Jetson AGX Xavier Series, Jetson Xavier NX, Jetson AGX Orin Series | Jetson Linux | Versions 35.1 and 34.1.1 | 35.2.1 |
| CVE‑2022‑42270 | NVIDIA Jetson AGX Xavier Series, Jetson Xavier NX, Jetson AGX Orin Series | Jetson Linux | 32.7.2 and prior releases | 32.7.3 |
### Get the Most Up to Date Product Security Information


Visit the [NVIDIA Product Security](https://www.nvidia.com/security) page to


* Subscribe to security bulletin notifications
* See the current list of NVIDIA security bulletins
* Report a potential security issue in any NVIDIA supported product
* Learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT)


### Revision History


| Revision | Date | Description |
|-----------:|:-----------------|:----------------|
| 1 | January 25, 2023 | Initial release |
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


* [ NVIDIA Jetson AGX Xavier Series, Jetson Xavier NX, Jetson TX1, Jetson TX2 Series (including Jetson TX2 NX), and Jetson Nano (including Jetson Nano 2GB) - March 2022](/app/answers/detail/a_id/5321/related/1)
* [ NVIDIA Jetson AGX Xavier Series, Jetson Xavier NX, Jetson TX1, Jetson TX2 Series (including Jetson TX2 NX) - April 2022](/app/answers/detail/a_id/5343/related/1)
* [ NVIDIA Data Plane Development Kit (MLNX\_DPDK) - August 2022](/app/answers/detail/a_id/5389/related/1)
* [ NVIDIA Jetson AGX Xavier Series, Jetson Xavier NX, Jetson TX1, Jetson TX2 Series (including Jetson TX2 NX), and Jetson Nano (including Jetson Nano 2GB)- August 2021](/app/answers/detail/a_id/5216/related/1)
* [ NVIDIA Jetson AGX Xavier Series, Jetson Xavier NX, Jetson TX1, Jetson TX2 Series (including Jetson TX2 NX), and Jetson Nano (including Jetson Nano 2GB) - June 2021](/app/answers/detail/a_id/5205/related/1)








