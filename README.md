# modbus_mitm

---

modbus_mitm 是一個工業控制（OT）網路連線的攻擊工具包，針對 modbus 協議進行竊聽與竄改等功能等功能

功能：

- interface 與 ip 掃描

- server 數據讀取與修改

- 利用中間人攻擊截斷 client 到 server 的封包

- （未完成）讓 client 連接到 fake server

## 使用

---

#### Requirement （python 套件）：

- tkinter

- psutil

- pyModbusTCP

- scapy

#### Requirement （外部工具）：

- ettercap

#### 開啟方式：

**程式還處於開發初期，須照著只是使用，否則可能會出現錯誤**

```python
python main.py
```

執行後將會開啟下方視窗

![](/home/hicat/.config/marktext/images/2024-07-15-23-55-49-image.png)

啟動後選擇 interface 並按 Scan IP，左下角的 Ready 會轉成 Scanning...，等到變回Ready即可在 Server 和 Client 選擇掃描到的 IP。

當選擇好 Server 就可以使用上方列的Server功能，填入 Bound 並選擇要讀取 coil 或 register，按下後及會在右下角空白處生成列表顯示左邊界到右邊界內的 coil 或 register 數據，可以直接修改其上面的數據（coil 請輸入 True、1 或 False、0，register 請輸入整數），填好要修改的數據後，即可按 Write Coils 或 Write Registers（Coils 或 Registers 須與讀取時一致）。

選擇好 Server 和 Client 後，即可按下 Start Mitm，此時會啟動 Server 和 Client 的中間人攻擊，並將 Client 發出的封包進行屏蔽。

Start Blank 預定是讓 Client 與 Fake Server 進行連線，但還未製作完成。