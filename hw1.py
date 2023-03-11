import math


def my_regula_falsi(f, xl, xh, max_error, max_iteration):
    # ilk başta xl ve xh arasında kök olup olmadığını kontrol edelim
    if f(xl) * f(xh) >= 0:
        return None, 0, None  # None değeri kökün bulunamadığını gösterir

    # iterasyon değişkenlerini tanımlayalım
    iteration = 0
    prev_xr = 0
    xr = xl

    # regula falsi yöntemini uygulayalım
    while True:
        iteration += 1

        # xr'yi hesaplayalım
        fxh = f(xh)
        fxl = f(xl)
        xr = xh - fxh * (xl - xh) / (fxl - fxh)

        # mutlak hatayı hesaplayalım
        if iteration > 1:
            error = abs((xr - prev_xr) / xr)
            if error <= max_error:
                return xr, iteration, error

        # yeni tahminimiz xl veya xh arasında kalmalıdır
        if f(xr) * f(xh) < 0:
            xl = xr
        else:
            xh = xr

        # max_iteration sayısına ulaşıldığında veya mutlak hata max_error'dan küçük olduğunda döngüyü kır
        if iteration == max_iteration:
            return xr, iteration, error


def my_newton(f, df, x0, max_hata, max_iter):
    # iterasyon değişkenlerini tanımlayalım
    iteration = 0
    prev_x = x0
    x = x0

    # newton yöntemini uygulayalım
    while True:
        iteration += 1

        # x'i hesaplayalım
        x = prev_x - f(prev_x) / df(prev_x)

        # mutlak hatayı hesaplayalım
        error = abs((x - prev_x) / x)

        # max_hata veya max_iter'a ulaşıldığında döngüyü kır
        if error <= max_hata or iteration == max_iter:
            return x, iteration, error

        # x'i prev_x'e ata
        prev_x = x


def my_secant(f, xl, xh, max_hata, max_iter):
    # iterasyon değişkenlerini tanımlayalım
    iteration = 0
    prev_x = xl
    curr_x = xh

    # secant yöntemini uygulayalım
    while True:
        iteration += 1

        # yeni tahminimizi hesaplayalım
        next_x = curr_x - (f(curr_x) * (curr_x - prev_x)) / \
            (f(curr_x) - f(prev_x))

        # mutlak hatayı hesaplayalım
        error = abs((next_x - curr_x) / next_x)

        # max_hata veya max_iter'a ulaşıldığında döngüyü kır
        if error <= max_hata or iteration == max_iter:
            return next_x, iteration, error

        # yeni tahminleri güncelleyelim
        prev_x = curr_x
        curr_x = next_x
