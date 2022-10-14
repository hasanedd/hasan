{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23\n",
      " 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47\n",
      " 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71\n",
      " 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95\n",
      " 96 97 98 99]\n",
      "[ -9   2  -6   0   0   5  -5  -9 -10  -4  -9  -6  -8  -5   7   4   3  -6\n",
      "  -2   5   4   7   4   3   1   4  -8   9  -1   6  -2   2   2   6   4  -3\n",
      "  -1   0  -5  -2   9   6   6  -3   1  -1  -8  -6   7   4  -2  -7  -6  -7\n",
      " -10   5  -8   6   4  -9   2  -3   5  -5   6   8  -2  -1 -10   5   7   5\n",
      "   9   5  -9  -5 -10   6   1  -9   9   4   8   6   8  -9   9   6  -3   0\n",
      "  -9   9  -3  -4  -6  -1   1   9   0  -8]\n"
     ]
    },
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
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from numpy.random import seed\n",
    "from numpy.random import randint\n",
    "def estimate_coef(x, y):\n",
    "\t# number of observations/points\n",
    "\tn = np.size(x)\n",
    "\n",
    "\t# mean of x and y vector\n",
    "\tm_x = np.mean(x)\n",
    "\tm_y = np.mean(y)\n",
    "\n",
    "\t# calculating cross-deviation and deviation about x\n",
    "\tSS_xy = np.sum(y*x) - n*m_y*m_x\n",
    "\tSS_xx = np.sum(x*x) - n*m_x*m_x\n",
    "\n",
    "\t# calculating regression coefficients\n",
    "\tb_1 = SS_xy / SS_xx\n",
    "\tb_0 = m_y - b_1*m_x\n",
    "\n",
    "\treturn (b_0, b_1)\n",
    "\n",
    "def plot_regression_line(x, y, b):\n",
    "\t# plotting the actual points as scatter plot\n",
    "\tplt.scatter(x, y, color = \"m\",\n",
    "\t\t\tmarker = \"o\", s = 30)\n",
    "\n",
    "\t# predicted response vector\n",
    "\ty_pred = b[0] + b[1]*x\n",
    "\n",
    "\t# plotting the regression line\n",
    "\tplt.plot(x, y_pred, color = \"g\")\n",
    "\n",
    "\t# putting labels\n",
    "\tplt.xlabel('x')\n",
    "\tplt.ylabel('y')\n",
    "\n",
    "\t# function to show plot\n",
    "\tplt.show()\n",
    "    \n",
    "    \n",
    "x=np.arange(100)\n",
    "print(x)\n",
    "y = randint(-10, 10, 100)\n",
    "print(y)\n",
    "b = estimate_coef(x, y)\n",
    "plot_regression_line(x, y, b)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
\
