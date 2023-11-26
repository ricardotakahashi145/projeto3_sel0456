{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOnuQC3n21ZP1XF7b7Hhph0",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ricardotakahashi145/projeto3_sel0456/blob/main/gen_hash.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "id": "3ei1Xj0goBkh"
      },
      "outputs": [],
      "source": [
        "import hashlib\n",
        "\n",
        "correct_password = 'ricardo123'\n",
        "wrong_password = 'ricardo321'\n",
        "hash_password = hashlib.sha256(correct_password.encode('utf-8')).hexdigest()\n",
        "\n",
        "with open('hash.txt', 'w') as f:\n",
        "    f.write(hash_password)\n",
        "\n",
        "with open('correct.txt', 'w') as f:\n",
        "    f.write(correct_password)\n",
        "\n",
        "with open('wrong.txt', 'w') as f:\n",
        "    f.write(wrong_password)\n"
      ]
    }
  ]
}