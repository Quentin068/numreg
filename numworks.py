def regression():
    # Petit nettoyage de depart
    print("\n" * 10)
    print("=== REGRESSION (Pas a Pas) ===")

    # --- 1. SAISIE ---
    try:
        print("\nEntrer X (espaces):")
        lx_str = input("> ")
        lx = [float(k) for k in lx_str.split()]

        print("Entrer Y (espaces):")
        ly_str = input("> ")
        ly = [float(k) for k in ly_str.split()]
    except:
        print("! Erreur de saisie !")
        return

    n = len(lx)
    if n != len(ly):
        print("! Erreur: Tailles diff !")
        return
    if n < 3:
        print("/!\\ Attention: n < 3")
        print("ANOVA impossible")
        # On continue quand meme pour a et b

    # --- 2. CALCULS PRELIMINAIRES ---
    mx = sum(lx) / n
    my = sum(ly) / n

    s_xx = 0
    s_xy = 0
    for i in range(n):
        s_xx += (lx[i] - mx) ** 2
        s_xy += (lx[i] - mx) * (ly[i] - my)

    if s_xx == 0:
        print("Erreur: X constant")
        return

    a = s_xy / s_xx
    b = my - a * mx

    # --- 3. BOUCLE POINT PAR POINT (MODE DIAPO) ---

    sc_res = 0
    sc_reg = 0
    sc_tot = 0

    for i in range(n):
        # -- Calculs du point --
        dx = lx[i] - mx
        dy = ly[i] - my

        dx2 = dx ** 2
        dxy = dx * dy

        y_ch = a * lx[i] + b
        res = ly[i] - y_ch
        res2 = res ** 2

        y_ch_my = y_ch - my
        ych_my2 = y_ch_my ** 2

        sc_res += res2
        sc_reg += ych_my2
        sc_tot += (ly[i] - my) ** 2

        # -- AFFICHAGE PAGE PAR PAGE --
        # On simule un effacement d'ecran
        print("\n" * 50)

        print("=== POINT " + str(i + 1) + " / " + str(n) + " ===")
        print("X=" + str(lx[i]) + " | Y=" + str(ly[i]))
        print("-" * 29)

        # Colonnes demandees
        print("x-mx : {:.3f}".format(dx))
        print("y-my : {:.3f}".format(dy))
        print("(x-mx)^2 : {:.3f}".format(dx2))
        print("(x-mx)(y-my) : {:.3f}".format(dxy))
        print("-" * 29)
        print("^y (Pred) : {:.3f}".format(y_ch))
        print("Residu (e) : {:.3f}".format(res))
        print("Residu^2 : {:.3f}".format(res2))
        print("Explic^2 : {:.3f}".format(ych_my2))
        print("-" * 29)

        # PAUSE
        input("EXE -> Point Suivant")

    # --- 4. RESULTATS GLOBAUX ---

    # Calculs finaux
    if sc_tot == 0:
        r2 = 1.0
    else:
        r2 = sc_reg / sc_tot

    ddl_reg = 1
    ddl_res = n - 2

    mc_reg = sc_reg / ddl_reg

    # Securite division
    if ddl_res > 0:
        mc_res = sc_res / ddl_res
    else:
        mc_res = 0

    if mc_res > 0.0000001:
        f_calc = mc_reg / mc_res
    else:
        f_calc = 9999.99

    mc_tot = sc_tot / (n - 1)

    # -- Page Resultats Generaux --
    print("\n" * 50)
    print("=== RESULTATS (1/2) ===")
    print("a (pente) = {:.3f}".format(a))
    print("b (ordon) = {:.3f}".format(b))
    print("Eq : y = {:.3f}x + {:.3f}".format(a, b))
    print("-" * 20)
    print("R2 = {:.3f}".format(r2))
    if r2 > 0:
        print("r  = {:.3f}".format(r2 ** 0.5))
    print("-" * 20)
    input("EXE -> Voir ANOVA")

    # -- Page ANOVA --
    print("\n" * 50)
    print("=== ANOVA (2/2) ===")
    print("SRC |    SC    |    MC")
    print("-" * 29)
    print("Reg | {:8.3f} | {:8.3f}".format(sc_reg, mc_reg))
    print("Res | {:8.3f} | {:8.3f}".format(sc_res, mc_res))
    print("Tot | {:8.3f} | {:8.3f}".format(sc_tot, mc_tot))
    print("-" * 29)

    if f_calc > 9000:
        print("Fc = Infini")
    else:
        print("Fc = {:.3f}".format(f_calc))
    print("=" * 29)


# Lancement
regression()