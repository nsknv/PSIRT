

 NVIDIA DCGM - March 2023
===========================================




 Updated 03/31/2023 03:00 PM



NVIDIA has released a software update for NVIDIA® Data Center GPU Manager (DCGM). The update addresses security issues that may lead to denial of service and data tampering. To protect your system, [download and install the latest DCGM release from the CUDA repositories](https://developer.nvidia.com/dcgm#Downloads).


Go to [NVIDIA Product Security](https://www.nvidia.com/security/).






---




### Details


This section provides a summary of potential vulnerabilities that this security update addresses and their impact. Descriptions use [CWE™](https://cwe.mitre.org/), and base scores and vectors use [CVSS v3.1](https://www.first.org/cvss/v3.1/user-guide) standards.


| CVE ID | Description | Base Score | Vector |
|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------:|:------------------------------------|
| CVE‑2023‑0208 | NVIDIA DCGM for Linux contains a vulnerability in HostEngine (server component) where a user may cause a heap-based buffer overflow through the bound socket. A successful exploit of this vulnerability may lead to denial of service and data tampering. | 8.4 | AV:L/AC:L/PR:L/UI:N/S:C/C:N/I:H/A:H |
The NVIDIA risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk to your local installation. NVIDIA recommends evaluating the risk to your specific configuration.


### Security Updates


The following table lists the NVIDIA software products affected, versions affected, and the updated version that includes this security update.


| CVE IDs Addressed | Software Product | Operating System | Affected Versions | Updated Version |
|:--------------------|:-------------------|:-------------------|:----------------------------|:------------------|
| CVE‑2023‑0208 | DCGM | Linux | All versions prior to 3.1.7 | 3.1.7 |
#### Notes


* Earlier software branch releases that support this product are also affected. If you are using an earlier branch release, upgrade to the latest branch release.


### Mitigations


See [Security Updates](#security-updates) for the version to install.


### Get the Most Up to Date Product Security Information


Visit the [NVIDIA Product Security](https://www.nvidia.com/security) page to


* Subscribe to security bulletin notifications
* See the current list of NVIDIA security bulletins
* Report a potential security issue in any NVIDIA supported product
* Learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT)


### Revision History


| Revision | Date | Description |
|-----------:|:---------------|:--------------------------------------|
| 2 | March 31, 2023 | Corrected the impact of CVE‑2023‑0208 |
| 1 | March 31, 2023 | Initial release |
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


* [ NVIDIA Jetson AGX Xavier Series, Jetson Xavier NX, Jetson AGX Orin Series - January 2023](/app/answers/detail/a_id/5442/related/1)
* [Security Notice: NVIDIA Response to OpenSSL Vulnerabilities - November 2022](/app/answers/detail/a_id/5405/related/1)
* [ NVIDIA GeForce Experience - January 2023](/app/answers/detail/a_id/5384/related/1)
* [ NVIDIA Omniverse Kit - January 2023](/app/answers/detail/a_id/5418/related/1)
* [ NVIDIA GPU Display Driver - August 2022](/app/answers/detail/a_id/5383/related/1)








