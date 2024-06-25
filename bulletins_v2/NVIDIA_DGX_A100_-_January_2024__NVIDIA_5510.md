

 NVIDIA DGX A100 - January 2024
=================================================




 Updated 01/25/2024 09:15 AM



NVIDIA has released a firmware security update for the NVIDIA DGX™ A100 system.


To protect your system, download and install this firmware update through the [NVIDIA Enterprise Support Portal](https://nvid.nvidia.com/dashboard/).


Go to [NVIDIA Product Security](https://www.nvidia.com/security/).






---




### Details


This section provides a summary of potential vulnerabilities that this security update addresses and their impact. The description uses [CWE™](https://cwe.mitre.org/), and the base score and vector use [CVSS v3.1](https://www.first.org/cvss/specification-document) standards.


 


| ('CVE ID', 'CVE-2023-31029', 'CVE-2023-31030', 'CVE-2023-31024', 'CVE-2023-25529', 'CVE-2023-25530', 'CVE-2023-31032', 'CVE-2023-31035', 'CVE-2023-31033', 'CVE-2023-31034', 'CVE-2023-31025', 'CVE-2023-31031') | ('Description', 'NVIDIA DGX A100 baseboard management controller (BMC) contains a vulnerability in the host KVM daemon, where an unauthenticated attacker may cause a stack overflow by sending a specially crafted network packet. A successful exploit of this vulnerability may lead to arbitrary code execution, denial of service, information disclosure, and data tampering.', 'NVIDIA DGX A100 BMC contains a vulnerability in the host KVM daemon, where an unauthenticated attacker may cause a stack overflow by sending a specially crafted network packet. A successful exploit of this vulnerability may lead to arbitrary code execution, denial of service, information disclosure, and data tampering.', 'NVIDIA DGX A100 BMC contains a vulnerability in the host KVM daemon, where an unauthenticated attacker may cause stack memory corruption by sending a specially crafted network packet. A successful exploit of this vulnerability may lead to arbitrary code execution, denial of service, information disclosure, and data tampering.', 'NVIDIA DGX H100 and DGX A100 BMC contains a vulnerability in the host KVM daemon, where an unauthenticated attacker may cause a leak of another user’s session token by observing timing discrepancies between server responses. A successful exploit of this vulnerability may lead to information disclosure, escalation of privileges, and data tampering.', 'NVIDIA DGX H100 and DGX A100 BMC contains a vulnerability in the KVM service, where an attacker may cause improper input validation. A successful exploit of this vulnerability may lead to code execution, denial of service, escalation of privileges, and information disclosure.', 'NVIDIA DGX A100 SBIOS contains a vulnerability where a user may cause a dynamic variable evaluation by local access. A successful exploit of this vulnerability may lead to denial of service.', 'NVIDIA DGX A100 SBIOS contains a vulnerability where an attacker may cause an SMI callout vulnerability that could be used to execute arbitrary code at the SMM level. A successful exploit of this vulnerability may lead to code execution, denial of service, escalation of privileges, and information disclosure.', 'NVIDIA DGX A100 BMC contains a vulnerability where a user may cause a missing authentication issue for a critical function by an adjacent network . A successful exploit of this vulnerability may lead to escalation of privileges, code execution, denial of service, information disclosure, and data tampering.', 'NVIDIA DGX A100 SBIOS contains a vulnerability where a local attacker can cause input validation checks to be bypassed by causing an integer overflow. A successful exploit of this vulnerability may lead to denial of service, information disclosure, and data tampering.', 'NVIDIA DGX A100 BMC contains a vulnerability where an attacker may cause an LDAP user injection. A successful exploit of this vulnerability may lead to information disclosure.', 'NVIDIA DGX A100 SBIOS contains a vulnerability where a user may cause a heap-based buffer overflow by local access. A successful exploit of this vulnerability may lead to code execution, denial of service, information disclosure, and data tampering.') | ('Vector', 'AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H', 'AV:L/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H', 'AV:N/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:H', 'AV:A/AC:H/PR:N/UI:N/S:C/C:H/I:H/A:N', 'AV:A/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H', 'AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H', 'AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H', 'AV:A/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H', 'AV:L/AC:H/PR:L/UI:R/S:C/C:L/I:L/A:H', 'AV:A/AC:L/PR:N/UI:N/S:U/C:H/I:N/A:N', 'AV:L/AC:L/PR:H/UI:N/S:U/C:L/I:L/A:L') | ('Base Score', '9.3', '9.3', '9.0', '8.0', '8.0', '7.5', '7.5', '6.8', '6.6', '6.5', '4.2') | ('Severity', 'Critical', 'Critical', 'Critical', 'High', 'High', 'High', 'High', 'Medium', 'Medium', 'Medium', 'Medium') | ('CWE', 'CWE-121', 'CWE-121', 'CWE-121', 'CWE-208', 'CWE-20', 'CWE-627', 'CWE-20', 'CWE-306', 'CWE-190', 'CWE-90', 'CWE-122') | ('Impacts', 'Code execution, denial of service, information disclosure and data tampering', 'Code execution, denial of service, information disclosure and data tampering', 'Code execution, denial of service, information disclosure and data tampering', 'Information disclosure, escalation of privileges and data tampering', 'Code execution, denial of service, escalation of privileges and information disclosure', 'Denial of service', 'Code execution, denial of services, escalation of privileges and information disclosure', 'Escalation of privileges, code execution, denial of service, information disclosure, and data tampering', 'Denial of service, information disclosure, data tampering', 'Information disclosure', 'Code execution, denial of service, information disclosure, and data tampering') |
|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
 


The NVIDIA risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk to your local installation. NVIDIA recommends consulting a security or IT professional to evaluate the risk to your specific configuration.



### Security Updates


The following tables list the NVIDIA systems affected, firmware versions affected, and the updated version that includes this security update.


Note: **To get the updated BMC and SBIOS versions listed in the tables, upgrade to the NVIDIA DGX A100 Firmware Update Container Version 23.12.1. Firmware updates are available through the [NVIDIA Enterprise Support Portal](https://nvid.nvidia.com/dashboard/).**






| ('CVE IDs Addressed', 'CVE‑2023‑31024 CVE‑2023‑31025 CVE‑2023‑31029 CVE‑2023‑31030 CVE‑2023‑31033 CVE‑2023‑25529 CVE‑2023‑25530', 'CVE‑2023‑31031 CVE‑2023‑31032 CVE‑2023‑31034 CVE‑2023‑31035') | ('Affected Product(s)', 'DGX A100', 'DGX A100') | ('Platform/OS', 'DGX A100', 'DGX A100') | ('Affected Version(s)', 'All BMC versions prior to 00.22.05', 'All SBIOS versions prior to 1.25') | ('Updated Version', '00.22.05', '1.25') |
|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------|-------------------------------------------|-----------------------------------------------------------------------------------------------------|-------------------------------------------|



### Get the Most Up to Date Product Security Information




Visit the [NVIDIA Product Security](https://www.nvidia.com/security) page to


* Subscribe to security bulletin notifications
* See the current list of NVIDIA security bulletins
* Report a potential security issue in any NVIDIA supported product
* Learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT)


### 


### Revision History


| Revision | Date | Description |
|-----------:|:-----------------|:-------------------------------------------------------------------------------|
| 1.2 | January 25, 2024 | Fixed updated version info for SBIOS |
| 1.1 | January 17, 2024 | Removed reference to DGX H100 security update. Issue was fixed in August 2023. |
| 1 | January 11, 2024 | Initial release |
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
* [ NVIDIA Jetson AGX Xavier Series, Jetson Xavier NX, Jetson TX1, Jetson TX2 Series (including Jetson TX2 NX), and Jetson Nano (including Jetson Nano 2GB) - June 2023](/app/answers/detail/a_id/5466/related/1)
* [ NVIDIA GPU Display Driver - March 2023](/app/answers/detail/a_id/5452/related/1)
* [ NVIDIA CUDA Toolkit - March 2023](/app/answers/detail/a_id/5446/related/1)








