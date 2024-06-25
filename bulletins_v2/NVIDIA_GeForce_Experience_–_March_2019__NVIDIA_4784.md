

 NVIDIA GeForce Experience – March 2019
=========================================================




 Updated 09/29/2021 01:10 PM



NVIDIA has released a software security update for NVIDIA® GeForce Experience™. This update addresses an issue that may lead to code execution, denial of service, or escalation of privileges. To protect your system, download and install this software update through the [GeForce Experience Downloads](https://www.geforce.com/geforce-experience/download) page.
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Go to [NVIDIA Product Security](https://www.nvidia.com/product-security/).
--------------------------------------------------------------------------






---




### Details


This section summarizes the potential impact that this security update addresses. Descriptions use [CWE™](https://cwe.mitre.org/), and base scores and vectors follow [CVSS V3](https://www.first.org/cvss/user-guide) standards.


| CVE | Description | Base Score | Vector |
|:--------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------:|:------------------------------------|
| CVE‑2019‑5674 | NVIDIA GeForce Experience contains a vulnerability when ShadowPlay or GameStream is enabled. When an attacker has access to the system and creates a hard link, the software does not check for hard link attacks. This behavior may lead to code execution, denial of service, or escalation of privileges. | 8.8 | AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H |
The NVIDIA risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk of your local installation. NVIDIA recommends consulting a security or IT professional to evaluate the risk to your specific configuration.


### Security Updates


The following table lists the software products and versions affected, and the updated versions that include this security update.


Download the updates from the [GeForce Experience Downloads](https://www.geforce.com/geforce-experience/download) page, or open the client to automatically apply the security update.


| CVE | Software Product | Operating System | Affected Versions | Updated Version |
|:--------------|:-------------------|:-------------------|:---------------------------|------------------:|
| CVE‑2019‑5674 | GeForce Experience | Windows | All versions prior to 3.18 | 3.18 |
**Notes:**


* Affected versions include the versions listed and all earlier branches and releases.
* If you are using an unsupported version or an earlier unsupported branch, upgrade to the latest supported version. To identify products that are no longer supported, contact [NVIDIA Support](https://www.nvidia.com/object/support.html).


### Mitigations


None. See [Security Updates](#security-updates) for the versions to install.


### Acknowledgements


CVE‑2019‑5674: NVIDIA thanks David Yesland of Rhino Security Labs for reporting this issue.


### Get the Most Up to Date Product Security Information


Visit the [NVIDIA Product Security](https://www.nvidia.com/security) page to


* Subscribe to security bulletin notifications
* See the current list of NVIDIA security bulletins
* Report a potential vulnerability in any NVIDIA supported product
* Learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT)


### Revision History


| Revision | Date | Description |
|-----------:|:---------------|:------------------------------------------|
| 2 | March 27, 2019 | Updated the description of CVE‑2019‑5674. |
| 1 | March 26, 2019 | Initial release |
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


* [ NVIDIA GeForce Experience - September 2018](/app/answers/detail/a_id/4725/related/1)
* [Security Notice: CPU Speculative Side Channel Vulnerabilities](/app/answers/detail/a_id/4609/related/1)
* [ NVIDIA GeForce Experience - December 2019](/app/answers/detail/a_id/4954/related/1)
* [ NVIDIA Driver Security Updates for CPU Speculative Side Channel Vulnerabilities](/app/answers/detail/a_id/4611/related/1)
* [ NVIDIA GeForce Experience - July 2020](/app/answers/detail/a_id/5038/related/1)








