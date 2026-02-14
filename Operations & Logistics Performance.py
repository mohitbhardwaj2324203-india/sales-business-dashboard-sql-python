{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "c8d91407-4e8a-428d-8e2c-633d15ff8ffe",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Connected Successfully!\n"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "from sqlalchemy import create_engine\n",
    "\n",
    "engine = create_engine(\n",
    "    \"mysql+pymysql://root:Macebox%401315@localhost:3306/project_business\"\n",
    ")\n",
    "\n",
    "conn = engine.connect()\n",
    "\n",
    "print(\"✅ Connected Successfully!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "756b6669-3fbd-46ae-8f55-5d8209d42de1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(20)"
      ]
     },
     "execution_count": 2,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Returns_order = pd.read_sql(\"\"\"\n",
    "        SELECT COUNT(Order_ID) as Returns_order FROM Returns_Table\n",
    "    \"\"\", conn)\n",
    "Returns = Returns_order.iloc[0,0]\n",
    "Returns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "31ab6fd2-7ddf-4d44-81ec-874c6c9b215a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "np.int64(20118)"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Total_order = pd.read_sql(\"\"\"\n",
    "        SELECT COUNT(Order_ID) as Returns_order FROM Orders_Table\n",
    "    \"\"\", conn)\n",
    "Total = Total_order.iloc[0,0]\n",
    "Total"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "459dc0c3-c5e4-4633-82e9-65ac294c51a5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.09941346058256288\n"
     ]
    }
   ],
   "source": [
    "return_rate = (Returns / Total)* 100\n",
    "print(return_rate)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "e56350ee-79ad-440a-8f1a-c901bf69ee0c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Return_Rate</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>0.09941</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Return_Rate\n",
       "0      0.09941"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "return_rate = pd.read_sql(\"\"\"\n",
    "    SELECT \n",
    "        (SELECT COUNT(Order_ID) FROM Returns_Table) * 100.0 /\n",
    "        (SELECT COUNT(Order_ID) FROM Orders_Table) AS Return_Rate\n",
    "\"\"\", conn)\n",
    "\n",
    "return_rate\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "b518acc9-d2a0-4945-82b6-a4ca7698b50b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Return_Reason</th>\n",
       "      <th>orders</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>Damaged Product</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Wrong Item</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Poor Quality</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Late Delivery</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Defective</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Not Satisfied</td>\n",
       "      <td>3</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>Wrong Size</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     Return_Reason  orders\n",
       "0  Damaged Product       4\n",
       "1       Wrong Item       3\n",
       "2     Poor Quality       3\n",
       "3    Late Delivery       3\n",
       "4        Defective       3\n",
       "5    Not Satisfied       3\n",
       "6       Wrong Size       1"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "return_reasons = pd.read_sql(\"\"\"\n",
    "    SELECT Return_Reason, COUNT(Order_ID) as orders FROM Returns_Table GROUP BY Return_Reason\n",
    "    \"\"\", conn)\n",
    "return_reasons"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "e44aa4d5-b39b-4eaf-ad9d-0028c8abfca2",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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kSNHxrmupW53795tb775pjVs2DCljg0AAAAAgJQPta+88kqc69HR0ZY/f35r27at9erVKzm7BAAAAAAgPKFWnY6B1FKxzzyLjskW6cMAAACIY+vgRpE+BAApNaf2vvvus0OHDp2x/ciRI+42AAAAAADSbKidNGmS/f3332ds17bJkyenxHEBAAAAAJCyw4+1Fq2aQumiSm2WLFmCt506dcpmz55tBQoUSMouAQAAAAAIT6jNnTu3RUVFuUvZsmXPuF3btVYtAAAAAABpLtQuXLjQVWnr1Klj06dPt7x58wZvy5w5sxUvXtwKFy6cGscJAAAAAMD5hdqaNWsGux8XK1bMVWYBAAAAAPBVoyhVZJcuXWr33nuvVatWzXbu3Om2v/nmm247AAAAAABpNtRq6HH9+vUta9astnLlSjt27JjbfuDAARs4cGBKHyMAAAAAACkXagcMGGCjR4+2cePGWaZMmYLbq1ev7kIuAAAAAABpNtSuX7/eatSoccb2XLly2V9//ZUSxwUAAAAAQOqE2kKFCtnGjRvP2K75tCVLlkzOLgEAAAAACE+o7dixoz3++OP29ddfuw7Iu3btsilTpli3bt3s4YcfTs4uAQAAAABI3SV9PE899ZSdPn3a6tata0ePHnVDkWNiYqxHjx7WoUOH5OwSAAAAAIDwVGpVnX3mmWds//79tnbtWvvqq69s7969bk7tpZdempxdAgAAAACQuqFWS/f06tXLqlat6jodz5492ypUqGA//vijlStXzkaMGGFdu3ZN+lEgzenbt69deeWVwevt2rWzpk2bRvSYAAAAAOC8Qm3v3r3t9ddftxIlStiWLVusefPm9sADD9grr7xiw4YNc9uefPJJSy8U5FSV1iVz5sxWunRp69+/v508eTIix7N9+3a77777rHDhwu54ihcv7uY279u3L9WfWx9YTJw4MXi9Vq1a1qVLl1R/XgAAAABIsTm106ZNs8mTJ1uTJk3csOMrrrjCBbzVq1e74JceNWjQwCZMmOCq1KpMd+rUya3Nq4p1ajh+/LgLrPFt3rzZbrjhBitbtqy98847bpi3KuSaxzxnzhw3BDxv3ryWWjS0HAAAAAB8XandsWOHValSxX1fsWJF1xxKw43Ta6AVvUYtYaSqqDo716tXzz766CN3259//mlt2rSxPHnyWLZs2axhw4a2YcOGOI+f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",
      "text/plain": [
       "<Figure size 1000x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "chat_return_reasons = return_reasons.sort_values(\n",
    "    by=\"orders\",\n",
    "    ascending=False\n",
    ")\n",
    "plt.figure(figsize=(10,5))\n",
    "plt.barh(chat_return_reasons['Return_Reason'], chat_return_reasons['orders'])\n",
    "plt.title(\"Return Reasons\")\n",
    "plt.xlabel('orders')\n",
    "plt.ylabel('Return_Reason')\n",
    "plt.xticks(rotation=45)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "bec081eb-d748-407f-94e1-2fd55579c9dc",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Region_ID</th>\n",
       "      <th>Net_Profit</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>R006</td>\n",
       "      <td>82773.20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>R005</td>\n",
       "      <td>56960.71</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>R004</td>\n",
       "      <td>56728.37</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>R008</td>\n",
       "      <td>46828.10</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>R001</td>\n",
       "      <td>42648.66</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>R002</td>\n",
       "      <td>24557.25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>R003</td>\n",
       "      <td>-16081.32</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  Region_ID  Net_Profit\n",
       "0      R006    82773.20\n",
       "1      R005    56960.71\n",
       "2      R004    56728.37\n",
       "3      R008    46828.10\n",
       "4      R001    42648.66\n",
       "5      R002    24557.25\n",
       "6      R003   -16081.32"
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "region_money = pd.read_sql(\"SELECT ot.Region_ID, SUM(ot.Profit) - SUM(rt.Refund_Amount) AS Net_Profit FROM Returns_Table rt JOIN Orders_Table ot ON ot.Order_ID = rt.Order_ID GROUP BY ot.Region_ID ORDER BY Net_Profit DESC\",conn)\n",
    "region_money"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "ec3797b1-9d15-4b7b-acf4-7742b6a11e17",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA1wAAAH5CAYAAACVqz+wAAAAOnRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjEwLjAsIGh0dHBzOi8vbWF0cGxvdGxpYi5vcmcvlHJYcgAAAAlwSFlzAAAPYQAAD2EBqD+naQAATsxJREFUeJzt3QmczWX/x//PMJbCDJJdhpSdRPkRSoS4qW4pUdmilDaiISGVvexZCi24cyttlJssKYRIlkSy75Vl7Ov5P97X//89/xlbY8zXMXNez8fjPMw55zvnXGe6mvm+v9d1fa6IQCAQMAAAAABAskuT/C8JAAAAABACFwAAAAD4hMAFAAAAAD4hcAEAAACATwhcAAAAAOATAhcAAAAA+ITABQAAAAA+IXABAAAAgE8IXAAAAADgEwIXAOCKuOuuu9wttfvoo4+sWLFili5dOsuaNWuomwMACDECFwCEiffff98iIiKCt8jISMuXL581b97ctm/fbqnV3LlzE3xuBaHChQvb448/bhs2bEjW9/rtt9/cz/PGG2+0d99910aPHp2srw8ASHkiQ90AAMCV1bNnTytUqJAdO3bMfvzxRxfEfvjhB1u1apVlzJjRt/edMWOGhdJzzz1nt912m508edKWLVvmwtC0adNs5cqVljdv3mQLd2fOnLHBgwdbkSJFkuU1AQApG4ELAMLMvffeaxUqVHBfP/HEE5YjRw7r27evffnll/bQQw/59r7p06e3UKpatao9+OCD7usWLVrYzTff7ELYBx98YJ07d76s1z58+LBlypTJ9uzZ4+4n51TCI0eO2LXXXptsrwcAuLKYUggAYU5BRP74449zpscpoGTPnt2NfCmkKZSdbcWKFXbnnXfaNddcY/nz57c33njDxo0b56bvbdq06aJruBRQWrVqZbly5XLvUbZsWReA4tNr6LUGDBjgRqU0XS9DhgxutGrJkiVJ/tx33323+3fjxo3Bx7755hv381B4ypIli9WrV89Wr16d4Ps0ZTBz5szu51W3bl13XNOmTS0mJsa6d+/ujrn++utdm3v06BH8vnfeecdKlizp2q4RtWeeecb279+f4LX18ylVqpQtXbrUqlWr5oJWly5dEvwMhg8f7qZE6rlatWrZ1q1bLRAI2Ouvv+5+/vrvcN9999nevXsTvPYXX3zhPo/eW23Qz1Hfc/r06fO2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",
      "text/plain": [
       "<Figure size 1000x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "chat_region_money = region_money.sort_values(\n",
    "    by=\"Net_Profit\",\n",
    "    ascending=False\n",
    ")\n",
    "plt.figure(figsize=(10,5))\n",
    "plt.barh(chat_region_money['Region_ID'], chat_region_money['Net_Profit'])\n",
    "plt.title(\"Region Performance\")\n",
    "plt.xlabel('Net_Profit')\n",
    "plt.ylabel('Region_ID')\n",
    "plt.xticks(rotation=45)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "ba53d81d-7ce2-4241-804b-69da4cda484b",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Return_ID</th>\n",
       "      <th>Shipping_Cost</th>\n",
       "      <th>Profit</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>RET0001</td>\n",
       "      <td>387.0</td>\n",
       "      <td>34343.08</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>RET0002</td>\n",
       "      <td>438.0</td>\n",
       "      <td>29153.28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>RET0003</td>\n",
       "      <td>217.0</td>\n",
       "      <td>23736.16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>RET0004</td>\n",
       "      <td>297.0</td>\n",
       "      <td>38269.88</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>RET0005</td>\n",
       "      <td>461.0</td>\n",
       "      <td>30088.77</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>RET0006</td>\n",
       "      <td>90.0</td>\n",
       "      <td>19690.86</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>6</th>\n",
       "      <td>RET0007</td>\n",
       "      <td>262.0</td>\n",
       "      <td>30731.42</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>7</th>\n",
       "      <td>RET0008</td>\n",
       "      <td>490.0</td>\n",
       "      <td>22135.62</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>RET0009</td>\n",
       "      <td>66.0</td>\n",
       "      <td>17842.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>9</th>\n",
       "      <td>RET0010</td>\n",
       "      <td>184.0</td>\n",
       "      <td>4241.96</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>10</th>\n",
       "      <td>RET0011</td>\n",
       "      <td>312.0</td>\n",
       "      <td>20117.28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>11</th>\n",
       "      <td>RET0012</td>\n",
       "      <td>187.0</td>\n",
       "      <td>8918.68</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>12</th>\n",
       "      <td>RET0013</td>\n",
       "      <td>62.0</td>\n",
       "      <td>28257.25</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>13</th>\n",
       "      <td>RET0014</td>\n",
       "      <td>480.0</td>\n",
       "      <td>13686.75</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>14</th>\n",
       "      <td>RET0015</td>\n",
       "      <td>183.0</td>\n",
       "      <td>3941.64</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>15</th>\n",
       "      <td>RET0016</td>\n",
       "      <td>317.0</td>\n",
       "      <td>38196.16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>16</th>\n",
       "      <td>RET0017</td>\n",
       "      <td>91.0</td>\n",
       "      <td>19837.20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>17</th>\n",
       "      <td>RET0018</td>\n",
       "      <td>122.0</td>\n",
       "      <td>28579.24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>18</th>\n",
       "      <td>RET0019</td>\n",
       "      <td>313.0</td>\n",
       "      <td>27017.24</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>19</th>\n",
       "      <td>RET0020</td>\n",
       "      <td>201.0</td>\n",
       "      <td>34930.50</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Return_ID  Shipping_Cost    Profit\n",
       "0    RET0001          387.0  34343.08\n",
       "1    RET0002          438.0  29153.28\n",
       "2    RET0003          217.0  23736.16\n",
       "3    RET0004          297.0  38269.88\n",
       "4    RET0005          461.0  30088.77\n",
       "5    RET0006           90.0  19690.86\n",
       "6    RET0007          262.0  30731.42\n",
       "7    RET0008          490.0  22135.62\n",
       "8    RET0009           66.0  17842.00\n",
       "9    RET0010          184.0   4241.96\n",
       "10   RET0011          312.0  20117.28\n",
       "11   RET0012          187.0   8918.68\n",
       "12   RET0013           62.0  28257.25\n",
       "13   RET0014          480.0  13686.75\n",
       "14   RET0015          183.0   3941.64\n",
       "15   RET0016          317.0  38196.16\n",
       "16   RET0017           91.0  19837.20\n",
       "17   RET0018          122.0  28579.24\n",
       "18   RET0019          313.0  27017.24\n",
       "19   RET0020          201.0  34930.50"
      ]
     },
     "execution_count": 10,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "Shipping_cost = pd.read_sql(\"\"\"\n",
    "            SELECT rt.Return_ID, SUM(ot.Shipping_Cost) as Shipping_Cost , SUM(ot.Profit) as Profit\n",
    "            FROM Orders_Table ot JOIN Returns_Table rt ON ot.Order_ID = rt.Order_ID GROUP BY rt.Return_ID\n",
    "        \"\"\",conn)\n",
    "Shipping_cost"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "72fa4304-3881-4b77-ba09-4baf6a523c04",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 1000x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "chat_Shipping_cost = Shipping_cost.sort_values(\n",
    "    by=\"Profit\",\n",
    "    ascending=False\n",
    ")\n",
    "\n",
    "plt.figure(figsize=(10,5))\n",
    "\n",
    "plt.scatter(chat_Shipping_cost['Shipping_Cost'],\n",
    "            chat_Shipping_cost['Profit'],\n",
    "            color='blue')\n",
    "\n",
    "plt.title(\"Shipping Cost vs Profit\")\n",
    "plt.xlabel('Shipping_Cost')\n",
    "plt.ylabel('Profit')\n",
    "\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "28943cc6-ee4c-4dca-99a2-8c70e517553a",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Order_Date</th>\n",
       "      <th>count</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2023-01-01</td>\n",
       "      <td>28</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2023-01-02</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>2023-01-03</td>\n",
       "      <td>23</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>2023-01-04</td>\n",
       "      <td>16</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>2023-01-05</td>\n",
       "      <td>14</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1091</th>\n",
       "      <td>2025-12-27</td>\n",
       "      <td>14</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1092</th>\n",
       "      <td>2025-12-28</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1093</th>\n",
       "      <td>2025-12-29</td>\n",
       "      <td>20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1094</th>\n",
       "      <td>2025-12-30</td>\n",
       "      <td>22</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1095</th>\n",
       "      <td>2025-12-31</td>\n",
       "      <td>11</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>1096 rows × 2 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "     Order_Date  count\n",
       "0    2023-01-01     28\n",
       "1    2023-01-02     11\n",
       "2    2023-01-03     23\n",
       "3    2023-01-04     16\n",
       "4    2023-01-05     14\n",
       "...         ...    ...\n",
       "1091 2025-12-27     14\n",
       "1092 2025-12-28     22\n",
       "1093 2025-12-29     20\n",
       "1094 2025-12-30     22\n",
       "1095 2025-12-31     11\n",
       "\n",
       "[1096 rows x 2 columns]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "orders_trend = pd.read_sql(\"\"\"SELECT Order_Date, COUNT(Order_ID) as count FROM Orders_Table GROUP BY Order_Date ORDER BY Order_Date\"\"\",conn)\n",
    "orders_trend"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "9e43616e-40c6-45ea-a2c1-9a78d13ed10c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 1000x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "chat_orders_trend = orders_trend.sort_values(\n",
    "    by=\"count\",\n",
    "    ascending=False\n",
    ")\n",
    "\n",
    "plt.figure(figsize=(10,5))\n",
    "\n",
    "plt.plot(chat_orders_trend['Order_Date'], chat_orders_trend['count'])\n",
    "\n",
    "plt.title(\"Orders Trend\")\n",
    "plt.xlabel('Order_Date')\n",
    "plt.ylabel('count')\n",
    "\n",
    "plt.show()\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
