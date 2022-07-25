{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8def0b17-6f94-49c4-a288-a8a0dc469c95",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\user\\AppData\\Local\\Temp\\ipykernel_7752\\435152088.py:19: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  af[\"transaction_date\"] = af[\"transaction_date\"].apply(cmonth)\n"
     ]
    }
   ],
   "source": [
    "import json\n",
    "import pandas as pd\n",
    "import re\n",
    "from datetime import datetime\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "#Opening the Json File\n",
    "with open(\"transaction-data-adhoc-analysis.json\") as f:\n",
    "    data = json.load(f)\n",
    "\n",
    "udata = pd.read_json('transaction-data-adhoc-analysis.json', orient='column')\n",
    "df = pd.DataFrame(udata)\n",
    "\n",
    "af = df[['name', 'transaction_date']]\n",
    "\n",
    "def cmonth(Date):\n",
    "    dates = datetime.strptime(Date, \"%Y/%m/%d\")\n",
    "    return dates.month\n",
    "af[\"transaction_date\"] = af[\"transaction_date\"].apply(cmonth)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "d218b7b2-42fc-43d2-9cc2-46d51fdd6d95",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\user\\AppData\\Local\\Temp\\ipykernel_7752\\4205839930.py:7: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  af['January'] = af['transaction_date'].apply(jan)\n",
      "C:\\Users\\user\\AppData\\Local\\Temp\\ipykernel_7752\\4205839930.py:14: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  af['February'] =af['transaction_date'].apply(feb)\n",
      "C:\\Users\\user\\AppData\\Local\\Temp\\ipykernel_7752\\4205839930.py:21: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  af['March'] =af['transaction_date'].apply(mar)\n",
      "C:\\Users\\user\\AppData\\Local\\Temp\\ipykernel_7752\\4205839930.py:28: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  af['April'] =af['transaction_date'].apply(apr)\n",
      "C:\\Users\\user\\AppData\\Local\\Temp\\ipykernel_7752\\4205839930.py:35: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  af['May'] =af['transaction_date'].apply(may)\n",
      "C:\\Users\\user\\AppData\\Local\\Temp\\ipykernel_7752\\4205839930.py:42: SettingWithCopyWarning: \n",
      "A value is trying to be set on a copy of a slice from a DataFrame.\n",
      "Try using .loc[row_indexer,col_indexer] = value instead\n",
      "\n",
      "See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy\n",
      "  af['June'] =af['transaction_date'].apply(jun)\n"
     ]
    }
   ],
   "source": [
    "#checks if a particular set of data falls under a specific month\n",
    "def jan(x):\n",
    "    if x == 1:\n",
    "        return 1\n",
    "    else:\n",
    "        return 0\n",
    "af['January'] = af['transaction_date'].apply(jan)\n",
    "\n",
    "def feb(x):\n",
    "    if x == 2:\n",
    "        return 1\n",
    "    else:\n",
    "        return 0\n",
    "af['February'] =af['transaction_date'].apply(feb)\n",
    "\n",
    "def mar(x):\n",
    "    if x == 3:\n",
    "        return 1\n",
    "    else:\n",
    "        return 0\n",
    "af['March'] =af['transaction_date'].apply(mar)\n",
    "\n",
    "def apr(x):\n",
    "    if x == 4:\n",
    "        return 1\n",
    "    else:\n",
    "        return 0\n",
    "af['April'] =af['transaction_date'].apply(apr)\n",
    "\n",
    "def may(x):\n",
    "    if x == 5:\n",
    "        return 1\n",
    "    else:\n",
    "        return 0\n",
    "af['May'] =af['transaction_date'].apply(may)\n",
    "\n",
    "def jun(x):\n",
    "    if x == 6:\n",
    "        return 1\n",
    "    else:\n",
    "        return 0\n",
    "af['June'] =af['transaction_date'].apply(jun)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "45fd772f-e891-40c0-966e-3488d2564cdd",
   "metadata": {},
   "outputs": [],
   "source": [
    "#makes a dataframe which contains the unique names of each individual as well as a list for each one containing the months in which they purchases\n",
    "#-------------------------------------------------------------------------------------------------------------------------------------------------\n",
    "#creates a dataframe that only contains data for a particular month\n",
    "jan=af.loc[:, af.columns.drop(['February', 'March', 'April', 'May', 'June'])]\n",
    "feb=af.loc[:, af.columns.drop(['January', 'March', 'April', 'May', 'June'])]\n",
    "mar=af.loc[:, af.columns.drop(['January','February', 'April', 'May', 'June'])]\n",
    "apr=af.loc[:, af.columns.drop(['January','February', 'March', 'May', 'June'])]\n",
    "may=af.loc[:, af.columns.drop(['January','February', 'March', 'April', 'June'])]\n",
    "jun=af.loc[:, af.columns.drop(['January','February', 'March', 'April', 'May'])]\n",
    "\n",
    "listofnames=af['name'].unique()\n",
    "peoplelist=list()\n",
    "\n",
    "#Dataframe that contains the name and list of months each customer bought in\n",
    "table = pd.DataFrame(listofnames,columns=['Name'])\n",
    "\n",
    "#Removes duplicates\n",
    "jan = jan.drop_duplicates()\n",
    "feb = feb.drop_duplicates()\n",
    "mar = mar.drop_duplicates()\n",
    "apr = apr.drop_duplicates()\n",
    "may = may.drop_duplicates()\n",
    "jun =jun.drop_duplicates()\n",
    "\n",
    "#Removes rows that did not purchase in a particular month\n",
    "jan = jan[jan['transaction_date']==1]\n",
    "feb = feb[feb['transaction_date']==2]\n",
    "mar = mar[mar['transaction_date']==3]\n",
    "apr = apr[apr['transaction_date']==4]\n",
    "may = may[may['transaction_date']==5]\n",
    "jun = jun[jun['transaction_date']==6]\n",
    "\n",
    "listofmonths=[jan,feb,mar,apr,may,jun]\n",
    "\n",
    "#Checks if a name is in the data for a particular month\n",
    "for name in listofnames:\n",
    "    personel=list()\n",
    "    if name in list(jan['name']):\n",
    "        personel.append(1)\n",
    "    if name in list(feb['name']):\n",
    "        personel.append(2)\n",
    "    if name in list(mar['name']):\n",
    "        personel.append(3)\n",
    "    if name in list(apr['name']):\n",
    "        personel.append(4)\n",
    "    if name in list(may['name']):\n",
    "        personel.append(5)\n",
    "    if name in list(jun['name']):\n",
    "        personel.append(6)\n",
    "    peoplelist.append(personel)\n",
    "table['Months']=peoplelist"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "765c4aab-731b-4024-94cd-41e5b3b9907f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#engaged customers\n",
    "ejan = 0\n",
    "efeb= 0\n",
    "emar= 0\n",
    "eapr = 0\n",
    "emay = 0\n",
    "ejun = 0\n",
    "for v in table['Months']:\n",
    "    if 1 in v:\n",
    "            if 2 in v:\n",
    "                efeb = efeb+1\n",
    "                if 3 in v:\n",
    "                    emar = emar+1\n",
    "                    if 4 in v:\n",
    "                        eapr = eapr+1\n",
    "                        if 5 in v:\n",
    "                            emay = emay+1\n",
    "                            if 6 in v:\n",
    "                                ejun = ejun+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "dacb1173-1e73-4ccb-9071-83e86940f345",
   "metadata": {},
   "outputs": [],
   "source": [
    "#repeat customers\n",
    "rjan= 0\n",
    "rfeb= 0\n",
    "rmar= 0\n",
    "rapr = 0\n",
    "rmay = 0\n",
    "rjun = 0\n",
    "for r in table['Months']:\n",
    "    if 1 in r:\n",
    "        if 2 in r:\n",
    "            rfeb = rfeb+1\n",
    "    if 2 in r:\n",
    "        if 3 in r:\n",
    "            rmar = rmar+1\n",
    "    if 3 in r:\n",
    "        if 4 in r:\n",
    "            rapr = rapr+1\n",
    "    if 4 in r:\n",
    "        if 5 in r:\n",
    "            rmay = rmay+1\n",
    "    if 5 in r:\n",
    "        if 6 in r:\n",
    "            rjun = rjun+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3577cc82-93d2-4a9f-9926-70d19d74da4f",
   "metadata": {},
   "outputs": [],
   "source": [
    "#inactive customers\n",
    "ijan= 0\n",
    "ifeb= 0\n",
    "imar= 0\n",
    "iapr = 0\n",
    "imay = 0\n",
    "ijun = 0\n",
    "for h in table['Months']:\n",
    "    if 1 in h:\n",
    "        if 2 not in h:\n",
    "            ifeb = ifeb+1\n",
    "        elif 2 in h:\n",
    "            if 3 not in h:\n",
    "                imar = imar+1\n",
    "            elif 3 in h:\n",
    "                if 4 not in h:\n",
    "                    iapr = iapr+1\n",
    "                elif 4 in h:\n",
    "                    if 5 not in h:\n",
    "                        imay = imay+1\n",
    "                    elif 5 in h:\n",
    "                        if 6 not in h:\n",
    "                            ijun = ijun+1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "0c5bed9b-6c14-4ae6-944d-a47f2d04c1db",
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
       "      <th>Month</th>\n",
       "      <th>Repeating Customers</th>\n",
       "      <th>Inactive Customers</th>\n",
       "      <th>Enganged Customers</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>January</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>February</td>\n",
       "      <td>5172</td>\n",
       "      <td>1416</td>\n",
       "      <td>5172</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>March</td>\n",
       "      <td>5216</td>\n",
       "      <td>1046</td>\n",
       "      <td>4126</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>April</td>\n",
       "      <td>5154</td>\n",
       "      <td>837</td>\n",
       "      <td>3289</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>May</td>\n",
       "      <td>5110</td>\n",
       "      <td>622</td>\n",
       "      <td>2667</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>June</td>\n",
       "      <td>5193</td>\n",
       "      <td>477</td>\n",
       "      <td>2190</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Month  Repeating Customers  Inactive Customers  Enganged Customers\n",
       "0   January                    0                   0                   0\n",
       "1  February                 5172                1416                5172\n",
       "2     March                 5216                1046                4126\n",
       "3     April                 5154                 837                3289\n",
       "4       May                 5110                 622                2667\n",
       "5      June                 5193                 477                2190"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "#Displaying the data\n",
    "FinalData={'Month':['January', 'February', 'March', 'April', 'May', 'June'],'Repeating Customers':[rjan, rfeb,rmar,rapr,rmay,rjun],\n",
    "           'Inactive Customers':[ijan,ifeb,imar,iapr,imay,ijun],'Enganged Customers':[ejan,efeb,emar,eapr,emay,ejun]}\n",
    "FinalFrame= pd.DataFrame(FinalData)\n",
    "FinalFrame"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "7fe2f4c1-ad45-4196-aeea-944e08bfb5c9",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "Classification = ['Repeating', 'Inactive', 'Engaged']\n",
    "Quantity = [rfeb,ifeb,efeb]\n",
    "\n",
    "plt.bar(Classification, Quantity)\n",
    "plt.title('Customer Classifications in February')\n",
    "plt.xlabel('Classification')\n",
    "plt.ylabel('Quantity')\n",
    "plt.show()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "9798821a-a14a-41d8-8cea-f3c5f2a3f4eb",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "Classification = ['Repeating', 'Inactive', 'Engaged']\n",
    "Quantity = [rmar,imar,emar]\n",
    "\n",
    "plt.bar(Classification, Quantity)\n",
    "plt.title('Customer Classifications in March')\n",
    "plt.xlabel('Classification')\n",
    "plt.ylabel('Quantity')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "9418baf9-8f24-4527-9154-b72707b331d1",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "Classification = ['Repeating', 'Inactive', 'Engaged']\n",
    "Quantity = [rapr,iapr,eapr]\n",
    "\n",
    "plt.bar(Classification, Quantity)\n",
    "plt.title('Customer Classifications in April')\n",
    "plt.xlabel('Classification')\n",
    "plt.ylabel('Quantity')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "8461b8f5-ceec-4913-aed2-804d2bb074ae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "Classification = ['Repeating', 'Inactive', 'Engaged']\n",
    "Quantity = [rmay,imay,emay]\n",
    "\n",
    "plt.bar(Classification, Quantity)\n",
    "plt.title('Customer Classifications in May')\n",
    "plt.xlabel('Classification')\n",
    "plt.ylabel('Quantity')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "e2859468-a9de-474a-8b49-683f17e1710f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "Classification = ['Repeating', 'Inactive', 'Engaged']\n",
    "Quantity = [rjun,ijun,ejun]\n",
    "\n",
    "plt.bar(Classification, Quantity)\n",
    "plt.title('Customer Classifications in June')\n",
    "plt.xlabel('Classification')\n",
    "plt.ylabel('Quantity')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e7e8597d-d73a-4884-8ae8-25d1ca0abfb5",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
