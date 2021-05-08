def linkspam(lis, times):
    import webbrowser as wb
    import random as r
    for _ in range(times):
        wb.open_new( r.choice(lis) )

link_list = ['https://youtu.be/dQw4w9WgXcQ', # Rickroll
    'https://youtu.be/Cj8n4MfhjUc', # Spanish Inquisition
    'https://youtu.be/Mg02NzsXrJk', # Muta laugh
    'https://youtu.be/kK7uljnAmQI', # Loud Indiam music earrape
    'https://youtu.be/vTIIMJ9tUc8', # Tunak Tunak Tun
    'https://youtu.be/o_LrHt4Hhhs', # Nono square
    'https://youtu.be/EKgGSf-xTMg', # Denver Laugh
    'https://youtu.be/St32aLCNMmQ', # Tongo pumped up kicks
    'https://youtu.be/0FmzeEcuEos', # NO U
    'https://youtu.be/feA64wXhbjo', # Shooting stars
    'https://youtu.be/3ejAMB3g_b8', # Paralyzer
    'https://youtu.be/e8jR-t9axFI', # BRUH
    'https://youtu.be/n2bKLqUKb9w', # I am glad I am finally returning home
    'https://youtu.be/7yh9i0PAjck', # Ievan Polkka
    'https://youtu.be/6xUnSVTh8fI', # Ameno
    'https://youtu.be/GdY8T48Dkh0', # Totinos hot pizza rolls
    'https://youtu.be/VJe6LLoGgR8', # The family friendly noose song
    'https://youtu.be/g3jCAyPai2Y', # Baka Mitai
    'https://youtu.be/Hy8kmNEo1i8', # Scatman
    'https://youtu.be/MtN1YnoL46Q', # The duck song
    'https://youtu.be/iuJDhFRDx9M', # Tokyo Drift song
    'https://youtu.be/J-fXTRHApRc', # The trumpet song thingy jazz
    'https://youtu.be/3Q8TSrDFG6w', # Ratatouille alternative ending
    'https://youtu.be/G-T3qKl6y-c', # Grubhub song
    'https://youtu.be/rR9qUm_WEfg'  # Weird creepy af "Hi Jim"
    ]


if __name__ == '__main__':
    import random as r
    rand_int = r.randint(1,50)
    print(rand_int)
    linkspam(link_list, rand_int)
