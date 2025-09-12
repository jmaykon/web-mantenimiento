async function marcarLeida(id) {
  await fetch(`/usuarios/notificacion/leida/${id}/?next=${window.location.pathname}`);
  location.reload();
}