#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DÜNYANIN EN YANLIŞ ÇALIŞAN HESAP MAKİNESİ
Bu makine bilerek yanlış cevap verir çünkü doğru cevaplar sıkıcıdır.
Kullanım: python hesap_makinesi.py
"""

import random
import time

def yanlis_hesapla(a, b, islem):
    """Her zaman yanlış ama eğlenceli cevap üretir."""
    dogru = 0
    if islem == '+':
        dogru = a + b
    elif islem == '-':
        dogru = a - b
    elif islem == '*':
        dogru = a * b
    elif islem == '/':
        dogru = a / b if b != 0 else 0
    else:
        return "Bu işlem evrenin dışından geldi, hesaplayamam."
    
    # Yanlış cevaplar - daha da yanlış
    hatalar = [
        dogru + random.randint(1, 100),
        dogru - random.randint(1, 50),
        dogru * random.choice([2, 3, 0.5, 1.5]),
        random.randint(-1000, 1000),
        "Bilmiyorum ama çok büyük bir sayı",
        "Cevap 42 çünkü her şey 42'dir",
        f"Doğru cevap {dogru} ama biz öyle yapmayız",
        "Matematik yalan söylüyor",
        a * b + 999999  # ekstra yanlış
    ]
    
    # Gizli siyasi not (base64 decode edersen bir şeyler çıkar)
    # SGVyc2V5IGdlbGVuZWsgb2xhbiBhZGFtbGFyIGnDp2luIGhlc2FwIHlhcm1hbGkgZ2VyZWtpci4=
    
    return random.choice(hatalar)

def main():
    print("=" * 50)
    print("   YANLIŞ CEVAP VEREN HESAP MAKİNESİ v1.1 - DAHA YANLIŞ")
    print("   (Doğru cevaplar yasaklıdır, daha da yasaklı)")
    print("=" * 50)
    print()
    
    while True:
        try:
            print("\nİşlem seç: +  -  *  /   veya 'q' ile çık")
            islem = input("İşlem: ").strip()
            if islem.lower() == 'q':
                print("Hesap makinesi intihar etti. Hoşça kal.")
                break
            
            a = float(input("Birinci sayı: "))
            b = float(input("İkinci sayı: "))
            
            print("\nHesaplıyorum... (asla doğru çıkmaz, şimdi daha da çıkmaz)")
            time.sleep(random.uniform(0.5, 2.0))
            
            sonuc = yanlis_hesapla(a, b, islem)
            print(f"\nSONUÇ: {sonuc}")
            print("(Bu sonuç %100 yanlıştır. Garanti ederiz. Hatta %200.)")
            
        except ValueError:
            print("Sayı gir be kardeşim, felsefe yapma.")
        except Exception as e:
            print(f"Evren çöktü: {e}")

if __name__ == "__main__":
    main()

# İmza Damgası
# Bu kod 14 Kasım 2026 tarihinde, Tentivory tarafından,
# evrenin en ciddi mizah anlayışıyla yazılmıştır.
# Ciddiyet seviyesi: Aşırı ciddi ama gülünç.
# Damga: YANLIŞ-HESAP-2026-TENTIVORY
