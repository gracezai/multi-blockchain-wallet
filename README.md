# multi-blockchain-wallet
Week 19 - Blockchain Python

# Multi-Blockchain Wallet in Python

## Background

Your new startup is focusing on building a portfolio management system that supports not only traditional assets
like gold, silver, stocks, etc, but crypto-assets as well! The problem is, there are so many coins out there! It's
a good thing you understand how HD wallets work, since you'll need to build out a system that can create them.

You're in a race to get to the market. There aren't as many tools available in Python for this sort of thing, yet.
Thankfully, you've found a command line tool, `hd-wallet-derive` that supports not only BIP32, BIP39, and BIP44, but
also supports non-standard derivation paths for the most popular wallets out there today! However, you need to integrate
the script into your backend with your dear old friend, Python.

Once you've integrated this "universal" wallet, you can begin to manage billions of addresses across 300+ coins, giving
you a serious edge against the competition.

In this assignment, however, you will only need to get 2 coins working: Ethereum and Bitcoin Testnet.
Ethereum keys are the same format on any network, so the Ethereum keys should work with your custom networks or testnets.

## Generate a Mnemonic and derive the wallet keys

![address](Images/multi_address.PNG)

## Send some transactions

**Bitcoin Testnet transaction**

Bitcoin Testnet address: `mttqBtUbCgJ26VFkth8vsfz2oVFZ3SBavR`

1. Fund the Bitcoin testnet

2. Send a transaction to another testnet address

![address](Images/fund_btctest_confirmation.PNG)