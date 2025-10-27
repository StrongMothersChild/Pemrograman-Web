<html>
<head>
    <title>Menghitung Gaji Bersih Karyawan</title>
</head>
    <h1>Menghitung Gaji Bersih Karyawan</h1>
    <?php
    $jam = 10;
    $menit = 16;
    $detik = 42;
    $jamkeDetik = $jam * 3600;
    $menitkeDetik = $menit * 60;
    $detikkeDetik = $detik;
    $totalDetik = $jamkeDetik + $menitkeDetik + $detikkeDetik;
    echo "<p>jika waktu ".$jam.":".$menit.":".$detik." di nyatakan dalam 
    satuan detik adalah : ".$totalDetik."</p>";
    ?>    
</body>
</html>
