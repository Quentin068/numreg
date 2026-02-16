from math import sqrt


def calculs_complets(x, y):
    n = len(x)
    if n != len(y):
        print("Erreur: Tailles differentes")
        return

    # --- 1. Moyennes ---
    mx = sum(x) / n
    my = sum(y) / n

    # --- 2. Calcul de a et b (Pente et Ordonnée) ---
    s_xx = 0
    s_xy = 0
    for i in range(n):
        s_xx += (x[i] - mx) ** 2
        s_xy += (x[i] - mx) * (y[i] - my)

    # Sécurité division par zéro
    if s_xx == 0:
        print("Erreur: X est constant")
        return

    a = s_xy / s_xx
    b = my - a * mx

    # --- 3. Initialisation des Sommes ---
    sc_res = 0  # Somme Carrés Résiduelle
    sc_reg = 0  # Somme Carrés Régression (Expliquée)
    sc_tot = 0  # Somme Carrés Totale

    # --- 4. Boucle : Détail ligne par ligne ---
    print("\n" + "=" * 20)
    print("DETAIL POINT PAR POINT")
    print("=" * 20)

    for i in range(n):
        # Ecarts simples
        xi_mx = x[i] - mx
        yi_my = y[i] - my

        # Carrés et produits croisés
        xi_mx_2 = xi_mx ** 2
        prod_xy = xi_mx * yi_my

        # Prédiction (y chapeau) et Résidus
        y_chap = a * x[i] + b
        res = y[i] - y_chap  # yi - ^yi
        res_2 = res ** 2  # (yi - ^yi)^2

        # Ecart modèle / moyenne
        ych_my = y_chap - my  # ^yi - y
        ych_my_2 = ych_my ** 2  # (^yi - y)^2

        # Mise à jour des sommes totales
        sc_res += res_2
        sc_reg += ych_my_2
        sc_tot += (y[i] - my) ** 2

        # --- Affichage compact pour l'écran ---
        print(f"--- Point {i + 1} ---")
        # x_i - x | y_i - y
        print(f"dx:{xi_mx:.2f} | dy:{yi_my:.2f}")
        # (x_i - x)^2 | (x_i-x)(y_i-y)
        print(f"dx2:{xi_mx_2:.2f}| dxy:{prod_xy:.2f}")
        # ^y_i | y_i - ^y_i (Residu)
        print(f"^y:{y_chap:.2f} | Res:{res:.2f}")
        # (y_i - ^y_i)^2 (SCRes partiel)
        print(f"Res2:{res_2:.2f}")
        # ^y_i - y | (^y_i - y)^2 (SCReg partiel)
        print(f"Expl:{ych_my:.2f} | Exp2:{ych_my_2:.2f}")

    # --- 5. Calculs ANOVA finaux ---
    ddl_reg = 1
    ddl_res = n - 2

    if ddl_res <= 0:
        print("Pas assez de points pour ANOVA")
        return

    mc_reg = sc_reg / ddl_reg
    mc_res = sc_res / ddl_res
    mc_tot = sc_tot / (n - 1)

    r2 = sc_reg / sc_tot
    fc = mc_reg / mc_res
    delta = sqrt(mc_res)  # Ecart-type résiduel (s)

    # --- 6. Affichage Global ---
    print("\n" + "=" * 20)
    print("RESULTATS GLOBAUX")
    print("=" * 20)
    print(f"a = {a:.4f}")
    print(f"b = {b:.4f}")
    print(f"R2 = {r2:.4f}")
    print("-" * 20)
    print("--- SC (Sommes) ---")
    print(f"SCReg = {sc_reg:.4f}")
    print(f"SCRes = {sc_res:.4f}")
    print(f"SCTot = {sc_tot:.4f}")
    print("-" * 20)
    print("--- MC (Moyennes) ---")
    print(f"MCReg = {mc_reg:.4f}")
    print(f"MCRes = {mc_res:.4f}")
    print(f"MCTot = {mc_tot:.4f}")
    print("-" * 20)
    print(f"Fc = {fc:.4f}")
    print(f"Delta (s) = {delta:.4f}")
    print("p = (Voir table Fisher)")


# --- INTERFACE UTILISATEUR ---
print("\n--- REGRESSION ---")
try:
    print("Entrer X (ex: 1 2 3 4):")
    cx = input("> ")
    lx = [float(v) for v in cx.split()]

    print("Entrer Y (ex: 2 4 5 4):")
    cy = input("> ")
    ly = [float(v) for v in cy.split()]

    calculs_complets(lx, ly)

except ValueError:
    print("Erreur de saisie !")
    print("Utilise l'ESPACE pour")
    print("séparer les nombres.")