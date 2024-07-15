Security Bulletin: NVIDIA BlueField Data Processing Unit - September 2023

**Answer ID: 5479**

NVIDIA has released a firmware update for NVIDIA BlueField Data Processing Unit. This update addresses security issues that may lead to escalation of privileges.

To protect your system, download and install this firmware update from the [<span class="underline">NVIDIA Networking Support</span>](https://network.nvidia.com/support/firmware/firmware-downloads/) page.

Go to [<span class="underline">NVIDIA Product Security</span>](https://www.nvidia.com/security/).

### Details

This section provides a summary of potential vulnerabilities that this security update addresses and their impact. Descriptions use [<span class="underline">CWE™</span>](https://cwe.mitre.org/), and base scores and vectors use [<span class="underline">CVSS v3.1</span>](https://www.first.org/cvss/specification-document) standards.

<table>
<thead>
<tr class="header">
<th><strong>CVE ID</strong></th>
<th><strong>Description</strong></th>
<th><strong>Base Score</strong></th>
<th><strong>CWE and Vector</strong></th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td>CVE-2023-25519</td>
<td>NVIDIA ConnectX Host Firmware for BlueField Data Processing Unit contains a vulnerability where a restricted host may cause an incorrect user management error. A successful exploit of this vulnerability may lead to escalation of privileges.</td>
<td>7.8</td>
<td><a href="https://cwe.mitre.org/data/definitions/286.html"><span class="underline">CWE- 286</span></a><br />
<a href="https://nvd.nist.gov/vuln-metrics/cvss/v3-calculator?vector=AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H"><span class="underline">AV:L/AC:L/PR:L/UI:N/S:U/C:H/I:H/A:H</span></a></td>
</tr>
</tbody>
</table>

The NVIDIA risk assessment is based on an average of risk across a diverse set of installed systems and may not represent the true risk to your local installation. NVIDIA recommends evaluating the risk to your specific configuration.

### Security Updates

The following table lists the NVIDIA products affected, versions affected, and the updated version that includes this security update.

| **CVE IDs Addressed** | **Affected Product** | **Affected Version(s)**          | **Updated Firmware Version**                 | **Updated Bluefield Bundle (BFB) Version** |
| --------------------- | -------------------- | -------------------------------- | -------------------------------------------- | ------------------------------------------ |
| CVE-2023-25519        | BlueField 1          | All versions after 18.24.1000    | Contact your NVIDIA Customer Program Manager | N/A                                        |
|                       | BlueField 2 LTS      | All versions prior to 24.35.3006 | 24.35.3006 or later                          | 3.9.5 or later                             |
|                       | BlueField 2 GA       | All versions prior to 24.38.1002 | 24.38.1002 or later                          | 4.2.0 or later                             |
|                       | BlueField 3 GA       | All versions prior to 32.38.1002 | 32.38.1002 or later                          | 4.2.0 or later                             |

### Acknowledgements

NVIDIA thanks Hugo Magalhaes from Oracle for reporting issue CVE-2023-25519.

### Get the Most Up to Date Product Security Information

Visit the [<span class="underline">NVIDIA Product Security</span>](https://www.nvidia.com/security) page to

  - > Subscribe to security bulletin notifications

  - > See the current list of NVIDIA security bulletins

  - > Report a potential security issue in any NVIDIA supported product

  - > Learn more about the vulnerability management process followed by the NVIDIA Product Security Incident Response Team (PSIRT)

### Revision History

| **Revision** | **Date**          | **Description** |
| ------------ | ----------------- | --------------- |
| 1.0          | September 7, 2023 | Initial release |

### Support

If you have any questions about this security bulletin, contact [<span class="underline">NVIDIA Support</span>](https://www.nvidia.com/object/support.html).

##### **Disclaimer**

ALL NVIDIA INFORMATION, DESIGN SPECIFICATIONS, REFERENCE BOARDS, FILES, DRAWINGS, DIAGNOSTICS, LISTS, AND OTHER DOCUMENTS (TOGETHER AND SEPARATELY, “MATERIALS”) ARE BEING PROVIDED “AS IS.” NVIDIA MAKES NO WARRANTIES, EXPRESS, IMPLIED, STATUTORY, OR OTHERWISE WITH RESPECT TO THE MATERIALS, AND ALL EXPRESS OR IMPLIED CONDITIONS, REPRESENTATIONS AND WARRANTIES, INCLUDING ANY IMPLIED WARRANTY OR CONDITION OF TITLE, MERCHANTABILITY, SATISFACTORY QUALITY, FITNESS FOR A PARTICULAR PURPOSE AND NON-INFRINGEMENT, ARE HEREBY EXCLUDED TO THE MAXIMUM EXTENT PERMITTED BY LAW.

Information is believed to be accurate and reliable at the time it is furnished. However, NVIDIA Corporation assumes no responsibility for the consequences of use of such information or for any infringement of patents or other rights of third parties that may result from its use. No license is granted by implication or otherwise under any patent or patent rights of NVIDIA Corporation. Specifications mentioned in this publication are subject to change without notice. This publication supersedes and replaces all information previously supplied. NVIDIA Corporation products are not authorized for use as critical components in life support devices or systems without express written approval of NVIDIA Corporation.
