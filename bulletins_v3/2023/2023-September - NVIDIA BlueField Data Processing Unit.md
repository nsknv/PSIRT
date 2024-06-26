# NVIDIA BlueField Data Processing Unit (Bulletin ID: 5479)



 NVIDIA BlueField Data Processing Unit - September 2023
=========================================================================




 Updated 09/11/2023 02:45 PM



NVIDIA has released a firmware update for the NVIDIA BlueField Data Processing Unit. This update addresses security issues that may lead to escalation of privileges. To protect your system, download and install this firmware update from the [NVIDIA Networking Support](https://network.nvidia.com/support/firmware/firmware-downloads/) page.


Go to [NVIDIA Product Security](https://www.nvidia.com/security/).


 






---




### Details


This section provides a summary of potential vulnerabilities that this security update addresses and their impact. Descriptions use [CWE™](https://cwe.mitre.org/), and base scores and vectors use [CVSS v3.1](https://www.first.org/cvss/specification-document) standards.




| \*\*CVE ID\*\* | \*\*Description\*\* | \*\*Base Score\*\* | \*\*Vector and CWE\*\* |
| --- | --- | --- | --- |
| CVE‑2023‑25519 | NVIDIA ConnectX Host Firmware for the BlueField Data Processing Unit contains a vulnerability where a restricted host may cause an incorrect user management error. A successful exploit of this vulnerability may lead to escalation of privileges. | 7.8 | [AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) [CWE-](https://cwe.mitre.org/data/definitions/927.html)[286](https://cwe.mitre.org/data/definitions/286.html) |


The NVIDIA risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk to your local installation. NVIDIA recommends consulting a security or IT professional to evaluate the risk to your specific configuration.


### Security Updates


The following tables list the NVIDIA systems affected, firmware versions affected, and the updated version that includes this security update.




| \*\*CVE IDs Addressed\*\* | Affected Product | \*\*Affected Versions\*\* | \*\*Updated Firmware Versions\*\* | \*\*Updated BFB Version\*\* |
| --- | --- | --- | --- | --- |
| CVE‑2023‑25519 | BlueField 1 | All versions after 18.24.1000 | Contact your NVIDIA Customer Program Manager | N/A |
| BlueField 2 LTS | All versions prior to 24.35.3006 | 24.35.3006 or later | 3.9.5 or later |
| BlueField 2 GA | All versions prior to 24.38.1002 | 24.38.1002 or later | 4.2.0 or later |
| BlueField 3 GA | All versions prior to 32.38.1002 | 32.38.1002 or later | 4.2.0 or later |


### 


### Acknowledgements


NVIDIA thanks Hugo Magalhaes from Oracle for reporting issue CVE-2023-25519.


### Get the Most Up to Date Product Security Information


Visit the [NVIDIA Product Security](https://www.nvidia.com/security) page to


* Subscribe to security bulletin notifications
* See the current list of NVIDIA security bulletins
* Report a potential security issue in any NVIDIA supported product
* Learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT)


### Revision History








| \*\*Revision\*\* | \*\*Date\*\* | \*\*Description\*\* |
| --- | --- | --- |
| 1.0 | September 6, 2023 | Initial release |


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


* [ NVIDIA DGX H100 - August 2023](/app/answers/detail/a_id/5473/related/1)
* [ NVIDIA GeForce NOW for Android - August 2023](/app/answers/detail/a_id/5476/related/1)
* [ NVIDIA GPU Display Driver - March 2023](/app/answers/detail/a_id/5452/related/1)
* [ NVIDIA GeForce Experience - January 2023](/app/answers/detail/a_id/5384/related/1)
* [ NVIDIA Jetson AGX Xavier Series, Jetson Xavier NX, Jetson AGX Orin Series - January 2023](/app/answers/detail/a_id/5442/related/1)








