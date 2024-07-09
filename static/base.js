
    // Script para abrir/fechar sidebar
    $(document).ready(function() {
        $('#sidebarToggle').click(function() {
            $('#sidebar').toggleClass('show');
        });
        $('#sidebarClose').click(function() {
            $('#sidebar').removeClass('show');
        });
    });

