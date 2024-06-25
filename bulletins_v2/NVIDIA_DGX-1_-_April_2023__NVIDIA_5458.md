

 NVIDIA DGX-1 - April 2023
============================================




 Updated 07/14/2023 09:15 AM



NVIDIA has released a security update for NVIDIA DGX-1 firmware. This update addresses an issue that may lead to arbitrary code execution, denial of service, escalation of privileges, information disclosure, data tampering, and SecureBoot bypass.


To protect your system, download and install this firmware update through the [NVIDIA Enterprise Support Portal](https://nvid.nvidia.com/dashboard/).


Go to [NVIDIA Product Security](https://www.nvidia.com/security/).






---




### Details


This section provides a summary of potential vulnerabilities that this security update addresses and their impact. Descriptions use [CWE™](https://cwe.mitre.org/), and base scores and vectors use [CVSS v3.1](https://www.first.org/cvss/specification-document) standards.




| \*\*CVE ID\*\* | \*\*Description\*\* | \*\*Base Score\*\* | \*\*Vector\*\* |
| --- | --- | --- | --- |
| CVE‑2023‑0209 | NVIDIA DGX-1 SBIOS contains a vulnerability in the Uncore PEI module, where authentication of the code executed by SSA is missing, which may lead to arbitrary code execution, denial of service, escalation of privileges, information disclosure, data tampering, and SecureBoot bypass. | 8.2 | [AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:H/UI:N/S:C/C:H/I:H/A:H) |
| CVE‑2023‑25505 | NVIDIA DGX-1 BMC contains a vulnerability in the IPMI handler of the AMI MegaRAC BMC, where an attacker with the appropriate level of authorization can cause a buffer overflow, which may lead to denial of service, information disclosure, or arbitrary code execution. | 7.8 | [AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H) |
| CVE‑2023‑25506 | NVIDIA DGX-1 contains a vulnerability in Ofbd in AMI SBIOS, where a preconditioned heap can allow a user with elevated privileges to cause an access beyond the end of a buffer, which may lead to code execution, escalation of privileges, denial of service and information disclosure. The scope of the impact of this vulnerability can extend to other components. | 7.5 | [AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:H/PR:H/UI:N/S:C/C:H/I:H/A:H) |
| CVE‑2023‑25507 | NVIDIA DGX-1 BMC contains a vulnerability in the SPX REST API, where an attacker with the appropriate level of authorization can inject arbitrary shell commands, which may lead to code execution, denial of service, information disclosure, and data tampering. | 7.2 | [AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:N/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:H) |
| CVE‑2023‑25508 | NVIDIA DGX-1 BMC contains a vulnerability in the IPMI handler, where an attacker with the appropriate level of authorization can upload and download arbitrary files under certain circumstances, which may lead to denial of service, escalation of privileges, information disclosure, and data tampering. | 6.7 | [AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:H/UI:N/S:U/C:H/I:H/A:N)H |
| CVE‑2023‑25509 | NVIDIA DGX-1 SBIOS contains a vulnerability in Bds, which may lead to code execution, denial of service, and escalation of privileges. | 6.0 | [AV:L/AC:L/PR:H/UI:N/S:U/C:N/I:H/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:H/UI:N/S:U/C:N/I:H/A:H) |


The NVIDIA risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk to your local installation. NVIDIA recommends consulting a security or IT professional to evaluate the risk to your specific configuration.


### Security Updates


The following table lists the NVIDIA server products affected, firmware versions affected, and the updated version that includes this security update.


To protect your system, download and install this firmware update through the [NVIDIA Enterprise Support Portal](https://nvid.nvidia.com/dashboard/).




| \*\*CVE IDs Addressed\*\* | \*\*Hardware Platform\*\* | \*\*System\*\* | \*\*Affected Versions\*\* | \*\*Updated Version\*\* |
| --- | --- | --- | --- | --- |
| CVE‑2023‑25505 CVE‑2023‑25508 CVE‑2023‑25507 | NVIDIA DGX-1 Servers | DGX-1 | All BMC versions prior to 3.39.3 | 3.39.30 |
| CVE‑2023‑0209 CVE‑2023‑25506 CVE‑2023‑25509 | NVIDIA DGX-1 Servers | DGX-1 | All SBIOS prior to S2W\\_3A13 | S2W\\_3A13 |


#### Notes


* Upgrade the NVIDIA DGX-1 firmware container to version 23.06.03 to get the updated firmware and SBIOS version listed in the table above. Firmware updates are available through the NVIDIA Enterprise Support Portal.


### Additional Information: Security Vulnerabilities Reported by Intel


The following table lists potential security vulnerabilities in some Intel processors that have been reported by Intel. These vulnerabilities may allow escalation of privileges or denial of service. They are addressed in DGX-1 SBIOSS2W\_3A13.




| \*\*CVE ID\*\* | \*\*Severity\*\* | \*\*Summary\*\* |
| --- | --- | --- |
| [CVE-2020-12357](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-12357) | High | Intel(R) Processors Privilege Escalation Vulnerability |
| [CVE-2020-8670](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8670) | High | Intel(R) Processors Privilege Escalation Vulnerability |
| [CVE-2020-8700](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-8700) | High | Intel(R) Processors Privilege Escalation Vulnerability |
| [CVE-2020-12359](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-12359) | High | Intel(R) Processors Privilege Escalation Vulnerability |
| [CVE-2020-12358](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-12358) | Medium | Intel(R) Processors Denial of Service Vulnerability |
| [CVE-2021-0095](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-0095) | Medium | Intel(R) Processors Denial of Service Vulnerability |
| [CVE-2020-12360](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-12360) | Medium | Intel(R) Processors Privilege Escalation Vulnerability |
| [CVE-2020-24486](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-24486) | Medium | Intel(R) Processors Denial of Service Vulnerability |


### Get the Most Up to Date Product Security Information


Visit the [NVIDIA Product Security](https://www.nvidia.com/security) page to


* Subscribe to security bulletin notifications
* See the current list of NVIDIA security bulletins
* Report a potential security issue in any NVIDIA supported product
* Learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT)


### Revision History








| \*\*Revision\*\* | \*\*Date\*\* | Description |
| --- | --- | --- |
| 2.0 | July 14, 2023 | Modified notes section with guidance to upgrade the NVIDIA DGX-1 firmware container to version 23.06.3.  Bulletin version 1.0 previously guided users to upgrade to 23.04.01. |
| 1.1 | April 19, 2023 | Modified CVE-2023-0209 description. |
| 1.0 | April 19, 2023 | Initial release |


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


* [ NVIDIA GPU Display Driver - March 2023](/app/answers/detail/a_id/5452/related/1)
* [ NVIDIA CUDA Toolkit - March 2023](/app/answers/detail/a_id/5446/related/1)
* [ NVIDIA GeForce Experience - January 2023](/app/answers/detail/a_id/5384/related/1)
* [ NVIDIA Jetson AGX Xavier Series, Jetson Xavier NX, Jetson AGX Orin Series - January 2023](/app/answers/detail/a_id/5442/related/1)
* [ NVIDIA Omniverse Kit - January 2023](/app/answers/detail/a_id/5418/related/1)








