# NVIDIA GPU Display Driver (Bulletin ID: 4841)



 NVIDIA GPU Display Driver - August 2019
==========================================================




 Updated 09/29/2021 02:10 PM



NVIDIA has released a software security update for the NVIDIA GPU Display Driver. This update addresses issues that may lead to local code execution, denial of service, or escalation of privileges. To protect your system, download and install this software update through [NVIDIA Driver Downloads](https://www.nvidia.com/Download/index.aspx)
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


Go to [NVIDIA Product Security](https://www.nvidia.com/product-security/).
--------------------------------------------------------------------------






---




### Details


This section summarizes the potential impact that this security update addresses. Descriptions use [CWE™](https://cwe.mitre.org/), and base scores and vectors use [CVSS V3](https://www.first.org/cvss/user-guide) standards.




This section summarizes the potential impact that this security update addresses. Descriptions use CWE™, and base scores and vectors use CVSS V3 standards.
| \*\*CVE\*\* | \*\*Description\*\* | \*\*Base Score\*\* | \*\*Vector\*\* |
| --- | --- | --- | --- |
| CVE‑2019‑5683 | NVIDIA Windows GPU Display Driver contains a vulnerability in the user mode video driver trace logger component. When an attacker has access to the system and creates a hard link, the software does not check for hard link attacks. This behavior may lead to code execution, denial of service, or escalation of privileges. | 8.8 | [AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:C/C:H/I:H/A:H) |
| CVE‑2019‑5684 | NVIDIA Windows GPU Display Driver contains a vulnerability in DirectX drivers, in which a specially crafted shader can cause an out of bounds access of an input texture array, which may lead to denial of service or code execution. | 7.8 | [AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H) |
| CVE‑2019‑5685 | NVIDIA Windows GPU Display Driver contains a vulnerability in DirectX drivers, in which a specially crafted shader can cause an out of bounds access to a shader local temporary array, which may lead to denial of service or code execution. | 7.8 | [AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:H/PR:L/UI:N/S:C/C:H/I:H/A:H) |
| CVE‑2019‑5686 | NVIDIA Windows GPU Display Driver contains a vulnerability in the kernel mode layer (`nvlddmkm.sys`) handler for `DxgkDdiEscape` in which the software uses an API function or data structure in a way that relies on properties that are not always guaranteed to be valid, which may lead to denial of service. | 5.6 | [AV:L/AC:H/PR:L/UI:N/S:C/C:N/I:N/A:H](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:H/PR:L/UI:N/S:C/C:N/I:N/A:H) |
| CVE‑2019‑5687 | NVIDIA Windows GPU Display Driver contains a vulnerability in the kernel mode layer (`nvlddmkm.sys`) handler for `DxgkDdiEscape` in which an incorrect use of default permissions for an object exposes it to an unintended actor, which may lead to information disclosure or denial of service. | 5.2 | [AV:L/AC:L/PR:L/UI:N/S:C/C:L/I:N/A:L](https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:C/C:L/I:N/A:L) |


The NVIDIA risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk of your local installation. NVIDIA recommends consulting a security or IT professional to evaluate the risk to your specific configuration.


### Security Updates


The following table lists the NVIDIA software products affected, versions affected, and the updated version available from nvidia.com that includes this security update. Download the updates from [NVIDIA Driver Downloads](https://www.nvidia.com/Download/index.aspx).


#### Windows




Windows
| \*\*Software Product\*\* | \*\*Operating System\*\* | \*\*Affected Versions\*\* | \*\*Updated Version\*\* |
| --- | --- | --- | --- |
| GeForce | Windows | All R430 versions prior to 431.60 | 431.60 |
| Quadro, NVS | Windows | All R430 versions prior to 431.70 | 431.70 |
| All R418 Versions prior to 426.00 | 426.00 |
| All R410 versions | 412.40 |
| All R390 versions prior to 392.56 | 392.56 |
| Tesla | Windows | All R418 versions | 426.00 |
| vGPU 4.x | Windows | vGPU software 4.8, which contains Windows driver version 370.35 | vGPU software 4.9, which contains Windows driver version 370.39 |
| vGPU 8.x | Windows | vGPU software 8.0, which contains Windows driver version 425.31 | vGPU software 8.1, which contains Windows driver version 426.04 |
| vGPU 9.x | Windows | vGPU software 9.0, which contains Windows driver version 431.02 | vGPU software 9.1, which contains Windows driver version 431.79 |


**Notes:**


* Your computer hardware vendor may provide you with Windows driver version 431.23, 425.85, or 412.39 which also contain the security update.
* The table above may not be a comprehensive list of all affected versions or branch releases and may be updated as more information becomes available.
* Earlier software branch releases that support these products are also affected. If you are using an earlier branch release, upgrade to the latest branch release.
* If you are using NVIDIA virtual GPU software, log in to the [NVIDIA Enterprise Application Hub](https://nvid.nvidia.com/dashboard/) to download the updates from the NVIDIA Licensing Center.
* **CVE‑2019‑5676** - This previously disclosed CVE is now also addressed in the R390 branch drivers update for Windows 10.This CVE does not affect driver packages provided by your hardware vendor and applies only to driver packages that are downloaded from the [NVIDIA Driver Downloads](https://www.nvidia.com/Download/index.aspx) public web page.


### Mitigations


None. See [Security Updates](#security-updates) for the versions to install.


### Acknowledgements


NVIDIA thanks Piotr Bania of Cisco Talos for reporting the following issues:


* CVE-2019-5684
* CVE-2019-5685


### Get the Most Up to Date Product Security Information


Visit the [NVIDIA Product Security](https://www.nvidia.com/security) page to


* Subscribe to security bulletin notifications
* See the current list of NVIDIA security bulletins
* Report a potential vulnerability in any NVIDIA supported product
* Learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT)


### Revision History




Revision History





| \*\*Revision\*\* | \*\*Date\*\* | \*\*Description\*\* |
| --- | --- | --- |
| 4.0 | September 23, 2019 | Added information about driver updates for the vGPU software 4,9 release. |
| 3.0 | August 29, 2019 | Added information about driver updates for the vGPU software 9.1 release. |
| 2.0 | August 14, 2019 | Added information about driver updates for the Quadro R410, Tesla R418, and vGPU software 8.1 releases. |
| 1.0 | August 2, 2019 | Initial release |


### Support


If you have any questions about this security bulletin, contact [NVIDIA Support](https://www.nvidia.com/object/support.html).


### Frequently Asked Questions (FAQs)


[How do I determine which NVIDIA display driver version is currently installed on my PC?](https://nvidia.custhelp.com/app/answers/detail/a_id/2039)


##### Disclaimer


ALL NVIDIA INFORMATION, DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS (TOGETHER AND SEPARATELY, “MATERIALS”) ARE BEING PROVIDED “AS IS.” NVIDIA MAKES NO WARRANTIES, EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE MATERIALS, AND ALL EXPRESS OR IMPLIED CONDITIONS, REPRESENTATIONS AND WARRANTIES, INCLUDING ANY IMPLIED WARRANTY OR CONDITION OF TITLE, MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT, ARE HEREBY EXCLUDED TO THE MAXIMUM EXTENT PERMITTED BY LAW.


Information is believed to be accurate and reliable at the time it is furnished. However, NVIDIA Corporation assumes no responsibility for the consequences of use of such information or for any infringement of patents or other rights of third parties that may result from its use. No license is granted by implication or otherwise under any patent or patent rights of NVIDIA Corporation. Specifications mentioned in this publication are subject to change without notice. This publication supersedes and replaces all information previously supplied. NVIDIA Corporation products are not authorized for use as critical components in life support devices or systems without express written approval of NVIDIA Corporation.










Is this answer helpful?
-----------------------



Yes
No







Answers others found helpful
----------------------------


* [ NVIDIA GPU Display Driver - February 2019](/app/answers/detail/a_id/4772/related/1)
* [ NVIDIA SHIELD TV – October 2018](/app/answers/detail/a_id/4704/related/1)
* [ NVIDIA GeForce Experience - September 2018](/app/answers/detail/a_id/4725/related/1)
* [ NVIDIA GPU Display Driver - November 2019](/app/answers/detail/a_id/4907/related/1)
* [ NVIDIA SHIELD TV Software Security Updates for Multiple Vulnerabilities](/app/answers/detail/a_id/4682/related/1)








