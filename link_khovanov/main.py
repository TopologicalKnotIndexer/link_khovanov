import javakh_interface
import pd_code_components
import pd_code_connected_sum
import pd_code_sanity


def _base_crossing_signs(pd_code: list[list[int]]) -> list[int]:
    node_count = 4 * len(pd_code)
    incidences: dict[int, list[int]] = {}
    for crossing_index, crossing in enumerate(pd_code):
        for slot, label in enumerate(crossing):
            incidences.setdefault(label, []).append(4 * crossing_index + slot)
    if any(len(nodes) != 2 for nodes in incidences.values()):
        raise ValueError("each PD label must occur exactly twice")

    other = [-1] * node_count
    for nodes in incidences.values():
        other[nodes[0]], other[nodes[1]] = nodes[1], nodes[0]
    outgoing = [-1] * node_count

    def orient(seed: int, direction: int) -> None:
        if outgoing[seed] != -1:
            if outgoing[seed] != direction:
                raise ValueError("inconsistent PD orientation")
            return
        outgoing[seed] = direction
        queue = [seed]
        for node in queue:
            crossing, slot = divmod(node, 4)
            for neighbor in (4 * crossing + ((slot + 2) % 4), other[node]):
                next_direction = 1 - outgoing[node]
                if outgoing[neighbor] == -1:
                    outgoing[neighbor] = next_direction
                    queue.append(neighbor)
                elif outgoing[neighbor] != next_direction:
                    raise ValueError("inconsistent PD orientation")

    for crossing_index in range(len(pd_code)):
        orient(4 * crossing_index + 2, 1)
    for nodes in incidences.values():
        if outgoing[nodes[0]] == -1:
            orient(nodes[0], 1)

    signs = []
    for index, (a, b, c, d) in enumerate(pd_code):
        if a == d or c == b:
            signs.append(-1)
        elif d == c or a == b:
            signs.append(1)
        else:
            signs.append(-1 if outgoing[4 * index + 3] else 1)
    return signs


def link_khovanov(pd_code: list[list[int]]) -> list[str]:
    """Return distinct integral Khovanov values over component orientations."""
    if not pd_code_sanity.sanity(pd_code):
        raise ValueError("invalid PD code")
    oriented = pd_code_connected_sum.normalize_pd_code(pd_code)[0]
    components = pd_code_components.get_components_from_pd_code(oriented)
    component_of = {label: index for index, component in enumerate(components) for label in component}
    base = _base_crossing_signs(oriented)
    sign_rows = []
    seen_rows = set()
    for mask in range(1 << max(0, len(components) - 1)):
        signs = base.copy()
        for index, (a, b, c, d) in enumerate(oriented):
            strand_a, strand_b = component_of[a], component_of[b]
            if strand_a != component_of[c] or strand_b != component_of[d]:
                raise ValueError("crossing strands are inconsistent with components")
            if strand_a != strand_b and bool(mask & (1 << strand_a)) != bool(mask & (1 << strand_b)):
                signs[index] = -signs[index]
        key = tuple(signs)
        if key not in seen_rows:
            seen_rows.add(key)
            sign_rows.append(signs)
    return sorted(set(javakh_interface.solve_signed_variants(oriented, sign_rows)))
