def regression():
    print("\n" * 5)
    print("=== REGRESSION (3 dec) ===")

    # --- 1. Saisie ---
    try:
        print("\nEntrer X (espaces):")
        lx = [float(k) for k in input("> ").split()]
        print("Entrer Y (espaces):")
        ly = [float(k) for k in input("> ").split()]
    except:
        print("! Erreur de saisie !")
        return

    n = len(lx)
    if n != len(ly) or n < 2:
        print("! Erreur taille !")
        return

    # --- 2. Calculs Moyennes ---
    mx = sum(lx) / n
    my = sum(ly) / n

    # --- 3. Calculs Pente (a) et Ordonnee (b) ---
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

    # --- 4. Boucle Détails (Affichage point par point) ---
    print("\n" + "=" * 29)
    print("   DETAIL PAR POINT")
    print("=" * 29)

    sc_res = 0
    sc_reg = 0
    sc_tot = 0

    for i in range(n):
        # Ecarts simples
        dx = lx[i] - mx
        dy = ly[i] - my

        # Carrés / Produits
        dx2 = dx ** 2
        dxy = dx * dy

        # Prédiction / Résidu
        y_ch = a * lx[i] + b
        res = ly[i] - y_ch
        res2 = res ** 2

        # Ecart expliqué
        y_ch_my = y_ch - my
        ych_my2 = y_ch_my ** 2

        # Sommes totales
        sc_res += res2
        sc_reg += ych_my2
        sc_tot += (ly[i] - my) ** 2

        # --- Affichage Bloc (3 décimales) ---
        print(f"------- Pt {i + 1} -------")
        # Ecarts simples
        print(f"dx :{dx:.3f} | dy :{dy:.3f}")
        # Carrés de X et Produit croisé
        print(f"dx²:{dx2:.3f} | dxy:{dxy:.3f}")
        # Prédiction et Résidu
        print(f"^y :{y_ch:.3f} | Res:{res:.3f}")
        # Termes pour ANOVA (Residu² et Expliqué²)
        print(f"Rs²:{res2:.3f} | Ex²:{ych_my2:.3f}")
        print("")

    # --- 5. Résultats ANOVA ---
    r2 = sc_reg / sc_tot

    # Degrés de liberté
    ddl_reg = 1
    ddl_res = n - 2

    mc_reg = sc_reg / ddl_reg
    mc_res = sc_res / ddl_res
    mc_tot = sc_tot / (n - 1)

    f_calc = mc_reg / mc_res

    print("\n" + "=" * 29)
    print("   RESULTATS GLOBAUX")
    print("=" * 29)
    print(f"moy x = {mx:.3f}")
    print(f"moy y = {my:.3f}")
    print(f"a (pente) = {a:.3f}")
    print(f"b (ordon) = {b:.3f}")
    print(f"Eq : y = {a:.3f}x + {b:.3f}")
    print(f"R² = {r2:.3f}")

    print("-" * 29)
    print(" TABLEAU ANOVA")
    print("-" * 29)
    # En-tête
    print("SRC |    SC    |    MC")
    print("-" * 29)
    # Lignes du tableau
    print(f"Reg | {sc_reg:8.3f} | {mc_reg:8.3f}")
    print(f"Res | {sc_res:8.3f} | {mc_res:8.3f}")
    print(f"Tot | {sc_tot:8.3f} | {mc_tot:8.3f}")
    print("-" * 29)
    print(f"Fc (Fisher) = {f_calc:.3f}")
    print("=" * 29)


# Lancement auto
regression()